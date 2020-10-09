import tkinter as tk
from tkinter import *
import os

root = tk.Tk()

root.geometry('1200x550')

v = tk.StringVar()

def result():
   os.system(f"python -m freegames.{v.get()}")


tk.Label(root,text="""Choose your favourite programming language:""",justify=tk.LEFT,padx=20).pack()

img1=PhotoImage(file="C:/Users/Dell/Desktop/SGP-7sem/img1.png")
img2=PhotoImage(file="C:/Users/Dell/Desktop/SGP-7sem/img1.png")
img3=PhotoImage(file="C:/Users/Dell/Desktop/SGP-7sem/img1.png")
img4=PhotoImage(file="C:/Users/Dell/Desktop/SGP-7sem/img1.png")


tk.Radiobutton(root,image=img1,padx=20,pady=40,height=120,variable=v,value='snake').pack()
tk.Label(root,text="""Snake""",justify=tk.LEFT,padx=20).pack()

tk.Radiobutton(root,image=img2,padx=20,pady=40,height=120,variable=v,value='pacman').pack()
tk.Label(root,text="""Pacman""",justify=tk.LEFT,padx=20).pack()

tk.Radiobutton(root,image=img3,padx=20,pady=40,height=120,variable=v,value='simonsays').pack()
tk.Label(root,text="""Simonsays""",justify=tk.LEFT,padx=20).pack()

tk.Radiobutton(root,image=img4,padx=20,pady=40,height=120,variable=v,value='memory').pack()
tk.Label(root,text="""Memory""",justify=tk.LEFT,padx=20).pack()


button = tk.Button(root, text='Play', width=25, command=result)
button.pack()

root.mainloop()
