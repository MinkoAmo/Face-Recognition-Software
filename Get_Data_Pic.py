import os
import cv2

def get_Data_Pic(name_Exist, ID_exist):
    images_List = []
    names_List = []
    for name, id in zip(name_Exist,ID_exist):
        path = './DuLieu./' + name + '_' + str(id)
        data_List = os.listdir(path)
        data_Person = []
        for j in data_List:
            imagesN = cv2.imread(f"{path}/{j}")
            data_Person.append(imagesN)
        images_List.append(data_Person)
        names_List.append(name + '_' + str(id))
    images_names = []
    images_names.append(images_List)
    images_names.append(names_List)
    return images_names

