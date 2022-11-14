import openpyxl
from Model import node_model
def GetNodes():
    wb = openpyxl.load_workbook(r"source")
    sheet = wb.active
    x = []
    y = []
    list_nodes = []
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
        for cell in row:
            if type(cell.value) is type(int()):
                list_nodes.append(node_model.Node(y[cell.row - 1], y[cell.column - 1], cell.value))

    return list_nodes