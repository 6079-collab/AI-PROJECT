import cv2
import numpy as np

def preprocess_image(image):

    img = cv2.resize(image,(224,224))

    # convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # blur to remove noise
    blur = cv2.GaussianBlur(gray,(5,5),0)

    # detect dark damaged areas
    _, mask = cv2.threshold(blur,120,255,cv2.THRESH_BINARY_INV)

    affected = np.sum(mask>0)
    total = mask.shape[0]*mask.shape[1]

    percent = (affected/total)*100

    return percent