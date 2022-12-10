import cv2
import face_recognition
import openpyxl
import os
from datetime import datetime
from Get_Data_Pic import get_Data_Pic
from Get_Name_ID_Exist import get_Name_ID_Exist
from Encode_Image import encode_Pic_Check
from tkinter import messagebox

def sign_In():
    #---Lấy ra danh sách tên và ID người dùng tồn tại
    name_Exist, ID_Exist = get_Name_ID_Exist('User.xlsx', 'Sheet1')

    #---Nhận dữ liệu từ kho ảnh
    images_List, names_List = get_Data_Pic(name_Exist, ID_Exist)

    #---Mã hóa kho ảnh
    encode_Pic_Check_List = encode_Pic_Check(images_List) #---Danh sách chứa ảnh đã mã hóa theo user

    #---Login
    cap = cv2.VideoCapture(0)
    confirm = False
    while True:
        ret, frame = cap.read()
        fram_Cur = cv2.resize(frame,(0,0),None,fx=1,fy=1)
        fram_Cur = cv2.cvtColor(fram_Cur, cv2.COLOR_BGR2RGB)
        encode_Face = face_recognition.face_encodings(fram_Cur) #---Mã hóa

        for encode_Cur_Face in encode_Face:
            for person in encode_Pic_Check_List:
                result = face_recognition.compare_faces(person, encode_Cur_Face, tolerance=0.35)
                if True in result:
                    confirm = True
                    name, id = names_List[encode_Pic_Check_List.index(person)].split("_")
                    #---Ghi vào trong excel login
                    now = datetime.now()
                    time_Now = now.strftime('%H:%M:%S')
                    date_Now = now.strftime('%d/%m/%Y')
                    #---Thêm dữ liệu vào Login_Log.xlsx và save
                    wb = openpyxl.load_workbook('Login_Log.xlsx')
                    sheet = wb['Sheet1']
                    row = (name, id, time_Now, date_Now)
                    sheet.append(row)
                    user_Path = './Login_Log.xlsx'
                    os.remove(user_Path)
                    wb.save('Login_Log.xlsx')
                    messagebox.showinfo('Notification', name + ' đã đăng nhập thành công')
            if confirm == True: break
        if confirm == True: break

        cv2.imshow('LOGIN', frame)
        if cv2.waitKey(1) == ord("q"):  # độ trễ 1/1000s , nếu bấm q sẽ thoát
            break
    cap.release()
    cv2.destroyAllWindows()
    if confirm == False:
        messagebox.showerror('ERROR',"Không nhận dạng được Face ID hoặc Face ID người dùng chưa tồn tại")

# sign_In()