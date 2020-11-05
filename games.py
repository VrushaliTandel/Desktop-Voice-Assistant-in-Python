import tkinter as tk
from tkinter import *
import os

root = tk.Tk()

root.geometry('850x550')


v = tk.StringVar()

def result():
   os.system(f"python -m freegames.{v.get()}")

tk.Label(root,text="""Choose One Game to Play:""",justify=tk.LEFT,padx=30,font='Helvetica 20 bold').pack()

img=PhotoImage(file="C:/Users/Dell/Desktop/SGP-7sem/play.png")
img1=PhotoImage(file="C:/Users/Dell/Desktop/SGP-7sem/img1.png")
img2=PhotoImage(file="C:/Users/Dell/Desktop/SGP-7sem/img2.png")
img3=PhotoImage(file="C:/Users/Dell/Desktop/SGP-7sem/img3.png")
img4=PhotoImage(file="C:/Users/Dell/Desktop/SGP-7sem/img4.png")


tk.Radiobutton(root,image=img1,padx=20,pady=40,height=80,variable=v,value='snake').pack()
tk.Radiobutton(root,image=img2,padx=20,pady=40,height=80,variable=v,value='pacman').pack()
tk.Radiobutton(root,image=img3,padx=20,pady=40,height=80,variable=v,value='simonsays').pack()
tk.Radiobutton(root,image=img4,padx=20,pady=40,height=80,variable=v,value='memory').pack()

button = tk.Button(root, text='Play',padx=80, width=75,height=75, command=result)
button.config(image=img)
button.pack()

root.mainloop()



