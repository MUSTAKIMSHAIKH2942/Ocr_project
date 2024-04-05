# Ocr_project
project to detect the number plate of a vehical using python code and ocr library 
OCR Project - README.md
This project provides a basic Optical Character Recognition (OCR) application using Python libraries.

Installation
Prerequisites:

Python 3.x (https://www.python.org/downloads/)
pip (usually comes bundled with Python)
Install required libraries:
Open a terminal or command prompt and navigate to your project directory. Then, run the following command:

Bash
pip install -r requirements.txt
Use code with caution.
This will install the necessary libraries (opencv-python and easyocr) listed in the requirements.txt file.

Usage
Run the script:
Open a terminal or command prompt and navigate to your project directory. Then, run the following command:

Bash
python main.py
Use code with caution.
This will execute the main.py script, which will prompt you to provide an image path or use a default image.

Select or provide an image:

The script will ask you to enter the path to an image file containing text.
Alternatively, you can leave the input blank to use a default image included in the project (if provided).
View the results:

The script will perform OCR on the image and display the extracted text on the console.
Project Structure
ocr_project/
├── requirements.txt   # List of required libraries
├── ocr_utils.py      # Contains the OCR function
└── main.py           # Main script for testing
requirements.txt: This file specifies the libraries needed for the project.
ocr_utils.py: This file contains the core function (perform_ocr) that handles image reading, OCR processing, and text extraction.
main.py: This is the main script that demonstrates how to use the perform_ocr function and displays the extracted text.
