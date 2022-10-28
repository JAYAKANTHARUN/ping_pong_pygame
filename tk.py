from tkinter import *
from PIL import ImageTk,Image
import os

root=Tk()

root.title("PING PONG GAME")

root.geometry("1500x800")
root.configure(bg="black")

image1=PhotoImage(file="tkimage.png")
root.iconphoto(False,image1)

label1=Label(root,text="PING PONG",font=("algerian",50),fg="red",bg="black").pack()

img=ImageTk.PhotoImage(Image.open("imagenew2.jpg"))
imagelabel=Label(root,image=img)
imagelabel.pack()

label2=Label(root,text="About the game :-")


root.mainloop()