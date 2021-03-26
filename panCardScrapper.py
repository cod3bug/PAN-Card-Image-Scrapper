# Importing packages
import cv2
import pytesseract
import re
import os
# Creating a list of names of Images existing in the pics folder
imgList= os.listdir("pics")
# Function which takes the name of the image present in pics folder and returns Pan Card details
def imgScan(photo):
    details= list()
    # Using OpenCV to read the Image 
    img = cv2.imread("./pics/"+photo)
    # Converting Image into Grayscale for pytesseract
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Storing the output in a string
    txt = pytesseract.image_to_string(grey)
    # Using Regex to find Date Of Birth and PAN
    dobRegex = re.compile(r'\d\d/\d\d/\d\d\d\d')
    details = dobRegex.findall(txt)
    allRegex = re.compile(r'[A-Z]{10}')
    allTxt = allRegex.findall(txt)
    panRegex = re.compile(r'[A-Z0-9]{10}')
    pan = panRegex.findall(txt)
    panCard = [x for x in pan if x not in allTxt]
    details.append(panCard)
    # If the orientation of image is not maintained there maybe be null values. Therefore this loop rotates the image everytime
    # there's a null value.
    i = 0
    while len(panCard)==0 & i < 3:
        image=cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
        grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        txt = pytesseract.image_to_string(grey)
        dobRegex = re.compile(r'\d\d/\d\d/\d\d\d\d')
        details = dobRegex.findall(txt)
        allRegex = re.compile(r'[A-Z]{10}')
        allTxt = allRegex.findall(txt)
        panRegex = re.compile(r'[A-Z0-9]{10}')
        pan = panRegex.findall(txt)
        panCard = [x for x in pan if x not in allTxt]
        details.append(panCard)
        i+=1
    return details


for l in imgList:
    result = imgScan(l)
    print("D.O.B of "+l+" : "+result[0]+" ; "+"PAN Number of "+l+" : "+result[1][0])