import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog


def load():
    root = tk.Tk()
    root.withdraw()

    file_types = [("Image files", "*.jpg *.jpeg *.bmoo *.tiff *.png *.gif")]

    image_path = filedialog.askopenfilename(title = "Selec a file", filetypes = file_types)

    if image_path:
        print("Selected file: ", image_path)
        img = cv.imread(image_path)

        img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        return img_rgb

    else:
        print("No file selected")

