## Pan Card Image Scrapping using OpenCV and Pytesseract
This tool can scrap out Date Of Birth and Permanent Account Number(PAN) from the image of PAN card.

### Image input format

The image file should have ".jpg" extension only and the image size must be less than 200Kb.

## Setup and Installation

* First clone this repository using :
```bash
git clone https://github.com/cod3bug/PAN-Card-Image-Scrapper.git
```
* Install all the necessary packages :
```bash
pip install -r requirements.txt
```
* For using Pytesseract you must have tesseract installed in your system(Windows, Linux, MacOS). To install it go through the official documentation in [Tesseract](https://tesseract-ocr.github.io/tessdoc/Home.html).
In, Ubuntu : 
```bash
sudo apt-get install tesseract-ocr
```
* Now, the only thing left to do is put all your images in **pics** folder and run the program.