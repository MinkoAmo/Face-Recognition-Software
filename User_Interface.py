import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from Login import sign_In
from Create_Data_By_Video import create_By_Video
from Create_Data_By_Webcam import create_By_Webcam


def temp_name_text(e):
   user_Name.delete(0,"end")
   user_Name.configure(fg='black')

def temp_pass_text(e):
   user_Pass.delete(0,"end")
   user_Pass.configure(fg='black')

def button_Login():
   sign_In()

def button_Video():
   create_By_Video()
   root.destroy()

def button_Webcam():
   create_By_Webcam()
   root.destroy()

def create_Acc():
   global root
   root = Tk()
   root.title('Create Account')
   root.geometry('500x200')
   Button(root, text="Create by Video", command=button_Video, font=('Arial', 14), bd=2).pack(side='left', padx=(50,0))
   Button(root, text="Create by Webcam", command=button_Webcam, font=('Arial', 14), bd=2).pack(side='right', padx=(0,50))

win = Tk()
win.title('User Interface')
win.geometry('986x617')

#---Background
image_Background = Image.open('./Image/Background.jpg')
backend = ImageTk.PhotoImage(image_Background)
background_Label = Label(win, image=backend)
background_Label.place(x=0, y=0)

user_Name = Entry(win, bg="white", width=30, font=('Arial', 14), borderwidth=10, fg='#808080', relief=tk.FLAT)
user_Name.insert(0, "User name")
user_Name.pack(ipady=3, pady=(175,3))
user_Name.bind("<FocusIn>", temp_name_text)

user_Pass = Entry(win, bg="white", width=30, font=('Arial', 14), borderwidth=10, fg='#808080', relief=tk.FLAT)
user_Pass.insert(0, "Password")
user_Pass.pack(ipady=3, pady=3)
user_Pass.bind("<FocusIn>", temp_pass_text)

button_Width = user_Pass['width']

login_Button = Button(win, text='LOGIN' , width=button_Width, font=('Arial', 14), fg='white', bg='#004aad', border=0)
login_Button.pack(ipadx= 0, ipady=3, pady=(30,0))

login_By_FaceID_Button = Button(win, text='LOGIN BY FACE ID',command=button_Login, width=button_Width, font=('Arial', 14), fg='white', bg='#2a4b6e', border=0)
login_By_FaceID_Button.pack(ipadx= 0, ipady=3, pady=(6,0))

signup_Button = Button(win, text='Create Account', font=('Arial', 10), fg='white',bg='#2a4b6e', border=2, command=create_Acc)
signup_Button.pack(side='left', ipadx=5, padx=(300,0), pady=(0,150))

needHelp_Button = Button(win, text='Need Help', font=('Arial', 10), fg='white',bg='#2a4b6e', border=2)
needHelp_Button.pack(side='left', ipadx=5, padx=(192,0), pady=(0,150))

win.mainloop()

