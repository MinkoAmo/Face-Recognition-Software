import cv2
import face_recognition
import os
import shutil
import openpyxl
from Get_Data_Pic import get_Data_Pic
from Get_Name_ID_Exist import get_Name_ID_Exist
from Encode_Image import encode_Pic_Check
from tkinter import filedialog as fd
from tkinter import messagebox
from tkinter import *
from Entry_Check import display
from Entry_Check import value

video_path = ''

def choose_File():
    filename = fd.askopenfilename(initialdir="./Video", title="Select A File", filetypes=[('MP4 file', '*.mp4')])
    global video_path
    video_path = os.path.abspath(filename)
    win_Cre.destroy()
    win_Cre.quit()


def create_By_Video():
    # ---Lấy ra danh sách tên và ID người dùng tồn tại
    name_Exist, ID_exist = get_Name_ID_Exist('User.xlsx', 'Sheet1')
    display()
    name_user, id_user = value

    # ---Thêm folder người dùng vào DuLieu
    path = './DuLieu/' + name_user + '_' + str(id_user)
    os.mkdir(path)

    # ---Tạo dữ liệu người dùng mới
    global win_Cre
    win_Cre = Tk()
    win_Cre.title('Create Data By Video')
    win_Cre.geometry('500x200')
    Label(win_Cre, bg="#808080", text='Choose a file .mp4 to create data', width=35, font=('Arial',14), borderwidth=10, fg='black', border=5).pack(pady=(50,3))
    Button(win_Cre, bg="#BBBBBB", command=choose_File, text='Click here', font=('Arial',10), borderwidth=10, fg='black', border=2).pack(pady=(5,0))
    win_Cre.mainloop()
    cap = cv2.VideoCapture(video_path)  # ---Đọc video
    i = 1

    while True:
        ret, frame = cap.read()
        framS = cv2.resize(frame,(0,0),None,fx=1,fy=1)
        cv2.imwrite(os.path.join(path, name_user + '_' + str(id_user) + '_' + str(i) + '.png'), frame)
        i += 1
        viTriF = face_recognition.face_locations(framS)  # ---Xác đinh vị trí khuôn mặt

        for viTriN in viTriF:  # Vẽ khung
            y1, x2, y2, x1 = viTriN
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        cv2.imshow('Creating Data', frame)
        if cv2.waitKey(1) == ord("q"):  # độ trễ 1/1000s , nếu bấm q sẽ thoát
            break
    cap.release()
    cv2.destroyAllWindows()

    # ---Nhận dữ liệu từ kho ảnh
    images_List, names_List = get_Data_Pic(name_Exist, ID_exist)

    # ---Mã hóa kho ảnh
    encode_Pic_Check_List = encode_Pic_Check(images_List)  # ---Danh sách chứa ảnh đã mã hóa theo user

    # ---Nhận dữ liệu người dùng mới
    pic_Of_New_User = []
    data_List = os.listdir(path)

    for i in data_List:
        img = cv2.imread(f"{path}/{i}")
        face_Loc = face_recognition.face_locations(img)
        if (face_Loc == []):
            del_path = path + '/' + i
            os.remove(del_path)
        else:
            pic_Of_New_User.append(img)

    # ---Mã hóa dữ liệu người dùng mới
    encode_Pic_Of_New_User = []
    for img in pic_Of_New_User:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode_Pic = face_recognition.face_encodings(img)[0]
        encode_Pic_Of_New_User.append(encode_Pic)

    # ---So sánh đối chiếu
    compare_Result = True
    for pic_User in encode_Pic_Of_New_User:
        for person in encode_Pic_Check_List:
            result = face_recognition.compare_faces(person, pic_User, tolerance=0.35)
            # ---Trường hợp người dùng đã đăng ký
            if True in result:
                compare_Result = False
                messagebox.showerror('ERROR', 'Face ID đã tồn tại')
            if compare_Result == False: break
        if compare_Result == False: break

    if compare_Result == False:
        shutil.rmtree(path)
    else:
        # ---Thêm dữ liệu vào .xlsx và save
        wb = openpyxl.load_workbook('User.xlsx')
        sheet = wb['Sheet1']
        row = (name_user, id_user)
        sheet.append(row)
        user_Path = './User.xlsx'
        os.remove(user_Path)
        wb.save('User.xlsx')
        messagebox.showinfo('Notification', "Đã thêm người dùng")

# create_By_Video()
