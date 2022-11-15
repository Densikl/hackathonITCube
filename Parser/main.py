import openpyxl
from Model import city_model

def GetNodes():
    wb = openpyxl.load_workbook(r"source")
    sheet = wb.active
    x = list()
    y = list()
    list_nodes = dict()
    count_x = 0
    for row in sheet.iter_rows():
        count_y = 0
        for cell in row:
            if count_x == 0:
                x.append(cell.value)
            if count_y == 0:
                y.append(cell.value)
            count_y+=1
        count_x+=1

    for row in sheet.iter_rows():
        tmp_city = list()
        start_city = str()
        for cell in row:
            if type(cell.value) is type(int()):
                tmp_city.append(city_model.City(x[cell.column - 1], cell.value))
                start_city = y[cell.row - 1]
        if start_city != '':
            list_nodes[start_city] = tmp_city

    return list_nodes