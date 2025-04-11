from pdf2image import convert_from_path
import os
import argparse

def convert_pdf_to_png(pdf_path, output_dir=None, dpi=300, single_file=False):
    """
    Convert a PDF file to PNG image(s).
    
    Args:
        pdf_path (str): Path to the PDF file
        output_dir (str, optional): Directory to save PNG files. Defaults to the same directory as PDF.
        dpi (int, optional): DPI for the output images. Higher DPI means better quality but larger files.
        single_file (bool, optional): If True, only convert the first page. If False, convert all pages.
    
    Returns:
        list: Paths to the generated PNG files
    """
    # Check if the PDF file exists
    if not os.path.isfile(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    
    # Set output directory
    if output_dir is None:
        output_dir = os.path.dirname(pdf_path)
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Get PDF file name without extension
    pdf_filename = os.path.splitext(os.path.basename(pdf_path))[0]
    
    # Convert PDF to images
    images = convert_from_path(pdf_path, dpi=dpi)
    
    output_paths = []
    
    # Save images
    if single_file:
        # Only convert the first page
        output_path = os.path.join(output_dir, f"{pdf_filename}.png")
        images[0].save(output_path, "PNG")
        output_paths.append(output_path)
        print(f"Converted first page of PDF to: {output_path}")
    else:
        # Convert all pages
        for i, image in enumerate(images):
            output_path = os.path.join(output_dir, f"{pdf_filename}_page_{i+1}.png")
            image.save(output_path, "PNG")
            output_paths.append(output_path)
        print(f"Converted {len(images)} pages from PDF to PNG in: {output_dir}")
    
    return output_paths

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Convert PDF to PNG")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("-o", "--output-dir", help="Directory to save PNG files")
    parser.add_argument("-d", "--dpi", type=int, default=300, help="DPI for output images (default: 300)")
    parser.add_argument("-s", "--single", action="store_true", help="Convert only the first page")
    
    args = parser.parse_args()
    
    try:
        convert_pdf_to_png(args.pdf_path, args.output_dir, args.dpi, args.single)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
