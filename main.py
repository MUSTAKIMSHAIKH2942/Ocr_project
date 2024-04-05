from ocr_utils import perform_ocr

# Test the OCR function with an image
# change path as per needed
extracted_text = perform_ocr("/Users/navroop/Desktop/text reco/ocr_project/__pycache__/image/image.jpeg")

print("Extracted Text:")
for text in extracted_text:
    print(text)
