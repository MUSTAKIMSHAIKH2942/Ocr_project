import cv2
import easyocr

def perform_ocr(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Initialize the OCR reader
    reader = easyocr.Reader(['en'])

    # Perform OCR on the image
    result = reader.readtext(img)

    # Extract and return the recognized text
    extracted_text = [entry[1] for entry in result]
    return extracted_text

