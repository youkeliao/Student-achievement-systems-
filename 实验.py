import analyze2
import model
import os
import student


def open_html2():
    f = open('a.txt', encoding='UTF-8')
    line = f.readline().strip()  # 读取第一行
    txt = []
    txt.append(line)
    while line:  # 直到读取完文件
        line = f.readline().strip()  # 读取一行文件，包括换行符
        txt.append(line)
    global name
    name = txt[0]
    global password
    password = txt[1]
    # print(name)
    # print(password)
    f.close()
    a = student.get_data(name=name, password1=password)
    # print(a)
    result = []
    for i in range(0, len(a)):
        result.append(a[i])
    result = result[2:11]
    print(result)
    result09 = []
    for j in range(0, len(result)):
        result09.append(int(result[j]))
    analyze2.students_self(result09)
    os.startfile(os.getcwd() + r"\你的水平vs顶尖水平.html")
    #     x = result[2:11]
    #     print(x)
    #     y = []
    #     for j in (0, len(x)):
    #         y.append(int(x[j]))
    #     print(y)
    #     return y
open_html2()

'''
item = QtWidgets.QTableWidgetItem()
self.tableWidget.setItem(0, 0, item)
item = QtWidgets.QTableWidgetItem()
self.tableWidget.setItem(0, 1, item)
item = QtWidgets.QTableWidgetItem()
self.tableWidget.setItem(0, 2, item)
item = QtWidgets.QTableWidgetItem()
self.tableWidget.setItem(0, 3, item)
item = QtWidgets.QTableWidgetItem()
self.tableWidget.setItem(0, 4, item)
item = QtWidgets.QTableWidgetItem()
self.tableWidget.setItem(0, 5, item)
item = QtWidgets.QTableWidgetItem()
self.tableWidget.setItem(0, 6, item)
item = QtWidgets.QTableWidgetItem()
self.tableWidget.setItem(0, 7, item)
item = QtWidgets.QTableWidgetItem()
self.tableWidget.setItem(0, 8, item)
item = QtWidgets.QTableWidgetItem()
self.tableWidget.setItem(0, 9, item)
item = QtWidgets.QTableWidgetItem()
self.tableWidget.setItem(0, 10, item)
item = QtWidgets.QTableWidgetItem()
self.tableWidget.setItem(0, 11, item)

item = self.tableWidget.item(0, 0)
item.setText(_translate("widget", f"{get_data(name=name, password1=password)[0]}"))
item = self.tableWidget.item(0, 1)
item.setText(_translate("widget", f"{get_data(name=name, password1=password)[1]}"))
item = self.tableWidget.item(0, 2)
item.setText(_translate("widget", f"{get_data(name=name, password1=password)[2]}"))
item = self.tableWidget.item(0, 3)
item.setText(_translate("widget", f"{get_data(name=name, password1=password)[3]}"))
item = self.tableWidget.item(0, 4)
item.setText(_translate("widget", f"{get_data(name=name, password1=password)[4]}"))
item = self.tableWidget.item(0, 5)
item.setText(_translate("widget", f"{get_data(name=name, password1=password)[5]}"))
item = self.tableWidget.item(0, 6)
item.setText(_translate("widget", f"{get_data(name=name, password1=password)[6]}"))
item = self.tableWidget.item(0, 7)
item.setText(_translate("widget", f"{get_data(name=name, password1=password)[7]}"))
item = self.tableWidget.item(0, 8)
item.setText(_translate("widget", f"{get_data(name=name, password1=password)[8]}"))
item = self.tableWidget.item(0, 9)
item.setText(_translate("widget", f"{get_data(name=name, password1=password)[9]}"))
item = self.tableWidget.item(0, 10)
item.setText(_translate("widget", f"{get_data(name=name, password1=password)[10]}"))
item = self.tableWidget.item(0, 11)
item.setText(_translate("widget", f"{get_data(name=name, password1=password)[11]}"))
'''
