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

label2=Label(root,text="\n\tABOUT THE GAME :-",font=("algerian",20),bg="black",fg="orange")
label3=Label(root,text="\t-> THIS IS A BASIC PING PONG GAME",font=("algerian",20),bg="black",fg="orange")
label4=Label(root,text="\t-> ITS A 1VS1 GAME",font=("algerian",20),bg="black",fg="orange")
label5=Label(root,text="\t-> FIRST PLAYER TO SCORE 5 POINTS WINS",font=("algerian",20),bg="black",fg="orange")
label6=Label(root,text="\t-> A RELAX TIME OF 3 SECONDS WILL BE GIVEN AT THE START AND ALSO AFTER EACH POINT",font=("algerian",20),bg="black",fg="orange")

label2.pack(anchor="w")
label3.pack(anchor="w")
label4.pack(anchor="w")
label5.pack(anchor="w")
label6.pack(anchor="w")

root.mainloop()