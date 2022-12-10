import cv2
import face_recognition

def encode_Pic_Check(images_List):
    encode_Pic_Check_List = []
    for i in images_List:
        pic_Of_Person = []
        for img in i:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode_Pic = face_recognition.face_encodings(img)[0]
            pic_Of_Person.append(encode_Pic)
        encode_Pic_Check_List.append(pic_Of_Person)
    return encode_Pic_Check_List