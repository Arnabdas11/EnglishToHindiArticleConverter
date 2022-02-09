# Converting English News article to Hindi text and audio 

## Preprocessing 

First, the news article has been scanned and then cropped properly.
Next, adaptive thresholding has been used for the ease of reading the text.
For the extraction of text from the Image, Tesseract-OCR has been used.

<img src="https://github.com/Arnabdas11/EnglishToHindiArticleConverter/blob/main/Repo/Women%20Tour/photo_2022-02-03_12-14-48.jpg" width="150" height="400">		<img src="https://github.com/Arnabdas11/EnglishToHindiArticleConverter/blob/main/Repo/Olympics/photo_2022-02-03_12-14-581.jpg" width="500" height="200">

After using Adaptive Threshold:

<img src="https://github.com/Arnabdas11/EnglishToHindiArticleConverter/blob/main/Repo/Women%20Tour/Thresholded%20(1).jpg" width="150" height="400">		<img src="https://github.com/Arnabdas11/EnglishToHindiArticleConverter/blob/main/Repo/Olympics/Thresholded.jpg" width="500" height="200">

## Text detected using Tesseract-OCR after fine tuning

https://github.com/Arnabdas11/EnglishToHindiArticleConverter/blob/main/Repo/Women%20Tour/Original%20(3).txt
https://github.com/Arnabdas11/EnglishToHindiArticleConverter/blob/main/Repo/Olympics/Original%20(3).txt

## English text Converted to Hindi using Facebook M2M model

https://github.com/Arnabdas11/EnglishToHindiArticleConverter/blob/main/Repo/Women%20Tour/Translated%20(2).txt
https://github.com/Arnabdas11/EnglishToHindiArticleConverter/blob/main/Repo/Olympics/Translated%20(2).txt

## Hindi audio using GTTS

https://github.com/Arnabdas11/EnglishToHindiArticleConverter/blob/main/Repo/Women%20Tour/hindi%20(6).mp3
https://github.com/Arnabdas11/EnglishToHindiArticleConverter/blob/main/Repo/Women%20Tour/hindi%20(6).mp3



P.S.- Tried to deploy it in Heroku but the slug size was too much. Any kind of feedback is appreciated. Thank You.
