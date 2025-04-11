# PDF to PNG Converter

A simple Python utility to convert PDF files to PNG images.

## Requirements

- Python 3.6+
- `pdf2image` library (which requires Poppler)
- `Pillow` library

## Installation

1. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Install Poppler:
   - **Windows**:
     - Download Poppler for Windows from https://github.com/oschwartz10612/poppler-windows
     - Extract the downloaded file to a location on your system
     - Add the `bin` folder to your PATH environment variable

   - **macOS**:
     ```
     brew install poppler
     ```

   - **Linux**:
     ```
     sudo apt-get install poppler-utils
     ```

## Usage

Basic usage to convert all pages of a PDF file:

```
python pdf_to_png_converter.py path_to_your_file.pdf
```

### Options

- `-o, --output-dir`: Directory to save PNG files (default: same directory as the PDF)
- `-d, --dpi`: DPI for output images (default: 300)
- `-s, --single`: Convert only the first page

### Examples

Convert all pages of a PDF with default settings:
```
python pdf_to_png_converter.py document.pdf
```

Convert only the first page:
```
python pdf_to_png_converter.py document.pdf --single
```

Convert with higher resolution (600 DPI) and save to a specific directory:
```
python pdf_to_png_converter.py document.pdf --dpi 600 --output-dir output_images
```

## Features

- Convert all pages or just the first page of a PDF
- Specify output directory
- Adjust resolution (DPI) of the output images
- Automatic filename generation based on the PDF name

## License

MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
