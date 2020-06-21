# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 17:25:00 2020

@author: Mohammed Sadiq
"""
import tkinter.ttk as ttk
from tkinter import Tk , mainloop, TOP , scrolledtext , Menu , filedialog , END,Label ,messagebox,simpledialog,colorchooser,messagebox
from tkinter import * 
import PIL
from PIL import Image,ImageDraw,ImageGrab,ImageTk

root = Tk()
root.title("Paint Application")
root.geometry('700x700')

#default brush color
brush_color="black"

def paint(e):
    
    #brush parameters
    brush_width='%0.0f' % float(myslider.get())
    #BRUSH TYPE:BUTT,ROUND,PROJECTING
    brush_type=brushtype.get()
    
    #starting position
    x1=e.x-1
    y1=e.y-1
    
    #Ending position
    x2=e.x+1
    y2=e.y+1
    
    #drawing on the canvas
    my_canvas.create_line(x1,y1,x2,y2,fill=brush_color,width=brush_width,capstyle=brushtype.get(),smooth=True)

#change brush size
def changebrushsize(thing):
    sliderlabel.config(text='%0.0f' % myslider.get())
 
#change brush color
def changebrushcolor():
    global brush_color
    brush_color="black"
    brush_color=colorchooser.askcolor(color=brush_color)[1]
    
#change canvas color
def changecanvascolor():
    global bg_color
    bg_color="black"
    bg_color=colorchooser.askcolor(color=bg_color)[1]
    my_canvas.config(bg=bg_color)
    
    
#clear screen
def clearscreen():
    my_canvas.delete(ALL)
    my_canvas.config(bg="white")

#save images as png
def saveaspng():
    result = filedialog.asksaveasfilename(initialdir='C:/Users/Mohammed Sadiq/Desktop',filetypes=(("png files","*.png"),("all files","*.*")))
    if result.endswith('.png'):
        pass
    else:
        result = result + '.png'
    
    if result:
        x=root.winfo_rootx() + my_canvas.winfo_x()
        y=root.winfo_rooty() + my_canvas.winfo_y()
        x1=x + my_canvas.winfo_width()
        y1=y + my_canvas.winfo_height()  
        ImageGrab.grab().crop((x,y,x1,y1)).save(result)
        messagebox.showinfo("Image saved", "your image has been saved !!")
        

#creating canvas    
w=600
h=400
my_canvas= Canvas(root, width=w, height=h, bg="white")
my_canvas.pack(pady=20);


my_canvas.bind('<B1-Motion>', paint)


#CREATING BRUSH OPTIONS FRAME
brushoptions_frame=Frame(root)
brushoptions_frame.pack(pady=20)


#brush Size
brushsizeframe=LabelFrame(brushoptions_frame,text="Brush Size")
brushsizeframe.grid(row=0,column=0,padx=50)

#brush slider
myslider=ttk.Scale(brushsizeframe,from_=1, to=100,command=changebrushsize,orient=VERTICAL,value=10)
myslider.pack(pady=10,padx=10)

#brush slider label
sliderlabel= Label(brushsizeframe, text=myslider.get())
sliderlabel.pack(pady=5)

#brush type
brushtype_frame=LabelFrame(brushoptions_frame,text="Brush Type",height=400)
brushtype_frame.grid(row=0,column=1,padx=50)

brushtype=StringVar()
brushtype.set("round")

#create radio buttons and brush type
brushtyperadio1=Radiobutton(brushtype_frame, text="Round",variable=brushtype,value="round")
brushtyperadio2=Radiobutton(brushtype_frame, text="Slash",variable=brushtype,value="butt")
brushtyperadio3=Radiobutton(brushtype_frame, text="Diamond",variable=brushtype,value="projecting")

brushtyperadio1.pack(anchor=W)
brushtyperadio2.pack(anchor=W)
brushtyperadio3.pack(anchor=W)

#change colors
changecolor_frame=LabelFrame(brushoptions_frame,text="Change Colors")
changecolor_frame.grid(row=0,column=2)

#change brush color button
brushcolorbutton=Button(changecolor_frame, text="Brush Color", command=changebrushcolor)
brushcolorbutton.pack(pady=10,padx=10)


#change canvas background color
canvascolorbutton=Button(changecolor_frame, text="Canvas Color", command=changecanvascolor)
canvascolorbutton.pack(pady=10,padx=10)

#program options 
options_frame=LabelFrame(brushoptions_frame,text="Program Options")
options_frame.grid(row=0,column=3,padx=50)


#clear screen button
clear_button=Button(options_frame,text="Clear Screen", command=clearscreen)
clear_button.pack(padx=10,pady=10)

#save image button
saveimage_button=Button(options_frame,text="Save to PNG",command=saveaspng)
saveimage_button.pack(padx=10,pady=10)










root.mainloop()