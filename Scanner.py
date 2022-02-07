# Importing the required libraries
from pytesseract import Output
import pytesseract
import cv2
import re


# Preprocessing the raw scanned image and doing adaptive thresholding
def preprocessing(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    adaptive_threshold = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 91, 26)
    return adaptive_threshold


# Scanning the thresholded image using Tesseract-OCR
def scanner(img):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    results = pytesseract.image_to_data(img, output_type=Output.DICT)
    text_list = []
    for i in range(0, len(results["text"])):
        x = results["left"][i]
        y = results["top"][i]
        w = results["width"][i]
        h = results["height"][i]
        text = results["text"][i]
        conf = int(float(results["conf"][i]))

    # filter out weak confidence text localizations
        if conf > 20:
            text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
            text_list.append(text)
    object_string = ' '.join([str(x) for x in text_list])

    # Substituting some characters as we observed and felt necessary, still some may have been left behind
    x = re.sub('- ', '', object_string)
    x = re.sub('-. ', '', x)
    x = re.sub('_ ', '', x)
    return object_string


