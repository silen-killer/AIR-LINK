from tkinter import *
from PIL import ImageTk,Image
m=Tk()
img=Image.open('bg.webp')
re_img=img.resize((1400,700))
bg=ImageTk.PhotoImage(re_img)
Label(m,image=bg).pack()
