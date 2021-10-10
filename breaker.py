import os
import xlrd
import csv

path = csv.writer(open(f"/home/user-104/PycharmProjects/Troshintest/Сетка/pathFilse.csv", 'w', newline=""))
pathFile=[[],[]]
fail_list = list(os.listdir('/home/user-104/PycharmProjects/Troshintest/Сетка/rawData'))
for fail in fail_list:
    wait = 0
    given = os.path.join('/home/user-104/PycharmProjects/Troshintest/Сетка/rawData',fail)
    sheet = xlrd.open_workbook(given).sheet_by_index(0) # тут и далее открываем xls файал и считываем сырые тестовые данные.
    number = 1
    col = csv.writer(open(f"/home/user-104/PycharmProjects/Troshintest/Сетка/testData/{fail[:-4]}{number}.csv", 'w',newline=""))
    for row in range(sheet.nrows):
        if type(sheet.row_values(row)[1])== type('a'):
            wait =1
            continue
        if (row-wait)%801 == 0:
            col = csv.writer(open(f"/home/user-104/PycharmProjects/Troshintest/Сетка/testData/{fail[:-4]}{number}.csv", 'w',newline=""))
            path.writerow([os.path.join('/home/user-104/PycharmProjects/Troshintest/Сетка/testData', f'{fail[:-4]}{number}.csv'),
                          os.path.join('/home/user-104/PycharmProjects/Troshintest/Сетка/ansData',f'{fail[:-4]}{number}.txt')])

            number += 1
        col.writerow(sheet.row_values(row)[-3:])  # как закрыть файл?









#number =1
#sheet = xlrd.open_workbook("/home/user-104/PycharmProjects/Troshintest/Сетка/test.xls").sheet_by_index(0) # тут и далее открываем xls файал и считываем сырые ПРОВЕРОЧНЫЕ данные.

#for row in range(((sheet.nrows-1)//181)):
#   col = csv.writer(open(f"/home/user-104/PycharmProjects/Troshintest/Сетка/rawData/test_{number}.csv", 'w', newline=""))
#   pathFile[number-1].append(f"/home/user-104/PycharmProjects/Troshintest/Сетка/rawData/test_{number}.csv")
#   number += 1
#   for element in range(181*row,181*(row+1),1):  # вроде чтение релу, а ниже сигмоиды или наоборот
#      col.writerow([sheet.row_values(element+1)[1]])
#   for element in range(181*row,181*(row+1),1):
#     col.writerow([sheet.row_values(element+1)[2]])
#

