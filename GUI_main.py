# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 14:27:05 2021

@author: om
"""

import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time
from tkvideo import tkvideo

global fn
fn = ""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="brown")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Pathological Myopia Detection")

canvas = tk.Canvas(root, width=900, height=50)
canvas.pack()

text = "Welcome to Myopia Eye Disease Detection using Deep Learning"
x = canvas.create_text(0, 25, text=text, anchor="w", font=('times',25,'bold italic'))

def scroll():
    canvas.move(x, -1, 0)  # Move text to the left
    if canvas.bbox(x)[0] < -canvas.winfo_width():
        canvas.move(x, canvas.winfo_width(), 0)  # Reset text position
    root.after(20, scroll)  # Schedule next scroll after 50 milliseconds

scroll()

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
video_label =tk.Label(root)
video_label.pack()
# read video to display on label
player = tkvideo("eye.mp4", video_label,loop = 1, size = (w, h))
player.play()
#


#################################################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


def reg():
    from subprocess import call
    call(["python","registration.py"])

def log():
    from subprocess import call
    call(["python","login.py"])
  
    
def window():
  root.destroy()


button1 = tk.Button(root, text="Login", command=log, width=14, height=1,font=('times', 20, ' bold '), bg="blue", fg="white")
button1.place(x=550, y=250)

button2 = tk.Button(root, text="Register",command=reg,width=14, height=1,font=('times', 20, ' bold '), bg="green", fg="white")
button2.place(x=550, y=350)

button3 = tk.Button(root, text="Exit",command=window,width=14, height=1,font=('times', 20, ' bold '), bg="red", fg="white")
button3.place(x=550, y=450)

root.mainloop()