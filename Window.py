# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 17:34:56 2024

@author: Yashraj Shinde
"""

import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Myopia Detection")
w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))



frame_alpr = tk.LabelFrame(root,width=1850, height=900, bd=5, font=('times', 14, 'bold'),bg="#152238")
frame_alpr.grid(row=0, column=0)
frame_alpr.place(x=0, y=0)

img = Image.open('eye.png')
img = img.resize((150,150), Image.LANCZOS)
logo_image = ImageTk.PhotoImage(img)

logo_label = tk.Label(root, image=logo_image)
logo_label.image = logo_image
logo_label.place(x=600, y=100)

lbl = tk.Label(root, text="Welcome to Myopia Detection \n Using Deep Learning", font=('times', 25,' bold underline '), height=2, width=45,bg="#152238",fg="white")
lbl.place(x=250, y=300)

def start():
    from subprocess import call
    call(['python','GUI_main.py'])
    
btn = tk.Button(root, text="Let's Begin", bg="Yellow",fg="Black",font=("",20), width=9, height=1, command=start)
btn.place(x=600, y=450)


root.mainloop()