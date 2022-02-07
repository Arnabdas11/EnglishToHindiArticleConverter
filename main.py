# Importing the required libraries and modules
import cv2
from transformers import pipeline
import Converter
import Scanner
from gtts import gTTS

# Getting the pipe ready
pipe = pipeline(task='text2text-generation', model='facebook/m2m100_418M')
# Getting the image file path
img = input("Please enter filename with path: ")


# Function for the translation of text from English to Hindi
def translator_text(img, pipe):
    img_new = cv2.imread(img)
    # Preprocessing the image
    preprocessed_img = Scanner.preprocessing(img_new)
    # Saving the thresholded image for future purposes
    cv2.imwrite("Thresholded.jpg", preprocessed_img)
    # Scanning and getting the dataframe
    text = Scanner.scanner(preprocessed_img)
    # Sentencing the text
    sentenced_text = Converter.sentencing(text)
    # The original text that was generated after scanning
    with open("Original.txt", "w") as f:
        f.write('. '.join(sentenced_text))
    # Converting the English text into Hindi text
    result_translate = Converter.converter(sentenced_text,pipe)
    return result_translate


# Function to translate the text to hindi speech
def translator_audio(new_result):
    obj = gTTS(text=new_result, slow=False, lang='hi')
    obj.save("hindi.mp3")


if __name__ == "__main__":
    result = translator_text(img, pipe)
    # Generating hindi text output of the original text
    new_result = '| '.join(result)
    with open("Translated.txt", "w", encoding='utf-8') as f:
        f.write(new_result)
    # Generating the hindi audio
    translator_audio(new_result)
