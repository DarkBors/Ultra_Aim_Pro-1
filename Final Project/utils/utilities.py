# utilities.py
# This file contains utility functions like performance metrics.

import tkinter as tk
from PIL import Image, ImageTk

def load_image(path, size=None):
    image = Image.open(path)
    if size:
        image = image.resize(size, Image.ANTIALIAS)
    return ImageTk.PhotoImage(image)
