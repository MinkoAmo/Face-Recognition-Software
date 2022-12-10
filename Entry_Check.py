from tkinter import *
from Get_Name_ID_Exist import get_Name_ID_Exist
from tkinter import messagebox

value = []

def temp_name_text_Cre(e):
   user_Name_Cre.delete(0,"end")
   user_Name_Cre.configure(fg='black')

def temp_id_text_Cre(e):
   user_ID_Cre.delete(0,"end")
   user_ID_Cre.configure(fg='black')

def check():
    name_Exist, ID_exist = get_Name_ID_Exist('User.xlsx', 'Sheet1')
    if (len(str(user_ID_Cre.get())) != 10 or user_ID_Cre.get() in ID_exist):
        messagebox.showerror('ERROR', 'Độ dài ID người dùng phải bằng 10 hoặc ID người dùng đã tồn tại')
    else:
        global value
        value.append(user_Name_Cre.get())
        value.append(user_ID_Cre.get())
        windown.destroy()
        windown.quit()

def get_Value():
    x, y = user_Name_Cre.get(), user_ID_Cre.get()
    return [x, y]

def display():
    global windown
    windown = Tk()
    windown.title('Create Account')
    windown.geometry('500x356')

    Label(windown, font=('Arial', 25), text='SIGN UP').pack(pady=(40,0))

    global user_Name_Cre
    user_Name_Cre = Entry(windown, bg="white", width=35, font=('Arial',14), borderwidth=10, fg='#808080', border=5)
    user_Name_Cre.insert(0, "User name")
    user_Name_Cre.pack(ipady=3, pady=(20,3))
    user_Name_Cre.bind("<FocusIn>", temp_name_text_Cre)

    global user_ID_Cre
    user_ID_Cre = Entry(windown, bg="white", width=35, font=('Arial', 14), borderwidth=10, fg='#808080', border=5)
    user_ID_Cre.insert(0, "ID")
    user_ID_Cre.pack(ipady=3, pady=3)
    user_ID_Cre.bind("<FocusIn>", temp_id_text_Cre)

    Button(windown, text='CREATE', width=20, font=('Arial', 14), fg='black', border=2, command=check).pack()

    windown.mainloop()

# display()
# print(value)








