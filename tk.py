from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import os

root=Tk()

r=IntVar()
r.set("1")

def startgame(number):
    if number==1:
        os.system("python cpu.py")
    if number==2:
        os.system("python 2p.py")
    if number==3:
        os.system("python 4p.py")        
 
def quitgame():
    messagebox.showinfo("Message","THANK YOU FOR PLAYING")
    root.destroy()  
    
def control():
    messagebox.showinfo("CONTROLS","MOVEMENT\nCPU -- W,S\n2 PLAYERS -- W,S/UPARROW,DOWNARROW\n4 PLAYERS -- W,S/UPARROW,DOWNARROW/O,P/N,M")      

root.title("PING PONG GAME")

root.attributes("-fullscreen",True)

root.configure(bg="black")

image1=PhotoImage(file="tkimage.png")
root.iconphoto(False,image1)

label1=Label(root,text="PING PONG",font=("algerian",50),fg="red",bg="black").pack()

img=ImageTk.PhotoImage(Image.open("imagenew2.jpg"))
imagelabel=Label(root,image=img)
imagelabel.pack()

label2=Label(root,text="\n\n\tABOUT THE GAME :-",font=("algerian",20),bg="black",fg="orange").pack(anchor="w")
label3=Label(root,text="\t-> THIS IS A BASIC PING PONG GAME",font=("algerian",20),bg="black",fg="orange").pack(anchor="w")
label4=Label(root,text="\t-> ITS A 1VS1 GAME",font=("algerian",20),bg="black",fg="orange").pack(anchor="w")
label5=Label(root,text="\t-> FIRST PLAYER TO SCORE 5 POINTS WINS",font=("algerian",20),bg="black",fg="orange").pack(anchor="w")
label6=Label(root,text="\t-> A RELAX TIME OF 3 SECONDS WILL BE GIVEN AT THE START AND ALSO AFTER EACH POINT\n",font=("algerian",20),bg="black",fg="orange").pack(anchor="w")

label10=Label(root,text="SELECT MODE : ",font=("algerian",20),bg="black",fg="orange").pack()

Radiobutton(root,text="CPU",variable=r,value=1,bg="yellow",width=10).pack()
Radiobutton(root,text="2 PLAYERS",variable=r,value=2,bg="yellow",width=10).pack()
Radiobutton(root,text="4 PLAYERS",variable=r,value=3,bg="yellow",width=10).pack()
label7=Label(root,text="\n",bg="black").pack()

button1=Button(root,text="\nCONTROLS\n",command=control,bg="lightgreen",width=20).pack()
label8=Label(root,text="\n",bg="black").pack()
button2=Button(root,text="\nSTART THE GAME\n",bg="lightgreen",command=lambda:startgame(r.get()),width=20).pack()
label9=Label(root,text="\n",bg="black").pack()
button3=Button(root,text="\nQUIT GAME\n",bg="lightgreen",command=quitgame,width=20).pack()

root.mainloop()