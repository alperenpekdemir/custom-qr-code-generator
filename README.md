# Custom QR Code Generator

A Python-based desktop application that generates customizable QR codes with optional logo integration. The application provides a simple graphical interface (Tkinter dialogs) for entering data, selecting a logo, and saving the generated QR code.

## Features
- Generate QR codes from user-provided links or text
- Optional logo/image integration in the center of the QR code
- Automatic logo resizing while preserving aspect ratio
- High error correction level (H) to ensure the QR code remains scannable even with a logo
- Custom gray color tone for a modern look
- User-friendly file dialogs for selecting a logo and saving the output
- Export the generated QR code as a PNG image

## Technologies Used
- Python 3
- `qrcode` — for QR code generation
- `Pillow (PIL)` — for image processing and logo placement
- `tkinter` — for GUI dialogs (input, file selection, save dialog)

## How It Works
1. The application opens a small input dialog asking for a link or text.
2. A QR code is generated with high error correction.
3. The user is asked to select a logo file (optional, PNG recommended).
4. If a logo is selected, it is automatically resized and placed at the center of the QR code.
5. The user chooses where to save the final QR code as a PNG file.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/alperenpekdemir/custom-qr-code-generator.git


Install the dependencies:
Bash

pip install -r requirements.txt
Run the project:
Bash

python qr_code.py
Requirements
Python 3.8+
qrcode
Pillow
tkinter comes pre-installed with most Python distributions and does not require separate installation.

Project Purpose
This project was developed to practice Python, work with external libraries (qrcode and Pillow), and build a small desktop utility with a simple GUI using tkinter.

Author
Alperen Pekdemir
