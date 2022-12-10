import openpyxl

def get_Name_ID_Exist(name_File, name_sheet):
    x = name_File
    y = name_sheet

    #---Truy cập file .xlsx
    wb = openpyxl.load_workbook(x)
    sheet = wb[y]

    #---Danh sách ID đã tồn tại
    ID_exist = []
    name_Exist = []

    column = sheet['A']
    for i in column[1:]:
        name_Exist.append(i.value)

    column = sheet['B']
    for i in column[1:]:
        ID_exist.append(i.value)

    name_ID = []
    name_ID.append(name_Exist)
    name_ID.append(ID_exist)
    return name_ID