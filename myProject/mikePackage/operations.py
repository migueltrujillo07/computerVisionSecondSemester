import cv2 as cv
import numpy as np
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt

def visualize(i, j):
    print('Visualize')

def negative(img_rgb):
  
    imgNegColor = 255 - img_rgb
    
    plt.figure(figsize=(15,8))

    plt.subplot(3, 3, 1)
    plt.imshow(imgNegColor)
    plt.axis('off')
    plt.title('Negative Image')
    plt.show()
    return imgNegColor

def gray_histogram(img):
    img_bgr = cv.cvtColor(img, cv.COLOR_RGB2BGR)
    gray_image = cv.cvtColor(img_bgr, cv.COLOR_BGR2GRAY)
    gray_hist = cv.calcHist([gray_image], [0], None, [256], [0, 256])
    return gray_image, gray_hist

def brighter(image ,constant_value):
    image_brightened = cv.add(image, constant_value)
    return image_brightened