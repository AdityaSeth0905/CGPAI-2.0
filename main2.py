import cv2 
import customtkinter as ctk
from customtkinter import *
import tkinter as tk
import os
import time
import face_recognition
from PIL import Image, ImageTk

def update_frame():
    ret, frame = cam.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        img = ImageTk.PhotoImage(image=img)
        lable.config(image=img)
        lable.image = img
    root.after(10, update_frame)



cam=cv2.VideoCapture(0)
ret, frame=cam.read()
root=CTk()
lable=tk.TkLabel("lOGIN window")
lable.pack()
root.title("CIIE")
root.geometry("500x500")
root.configure(background="dark")

if cv2.waitKey(1)==ord("q"):
    cv2.release()


root.mainloop()