import tkinter as tk
from tkinter import ttk, LEFT, END
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re


##############################################+=============================================================
root = tk.Tk()
root.configure(background="gray")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("1900x1450")
root.title("Accuracy Graph")


lbl = tk.Label(root, text="Graph of Myopia Detection using CNN Algorithm", font=('times', 25,' bold '), height=1, width=75,bg="maroon",fg="white")
lbl.place(x=0, y=3)

lbl = tk.Label(root, text="Accuracy of this project is above 90% ",font=('times', 20,' bold  italic'), height=1, width=45,bg="gray",fg="white")    
lbl.place(x=350, y=100)
# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('accuracy.png')
image2 = image2.resize((600,500))
background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image
background_label.place(x=130, y=170)  # , relwidth=1, relheight=1)



image2 = Image.open('loss.png')
image2 = image2.resize((500,500))
background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image
background_label.place(x=790, y=170)  # ,




root.mainloop()