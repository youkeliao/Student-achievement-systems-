# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2019/5/18  16:51
# 文件名称   ：实例_05.py
# 开发工具   ：PyCharm
# -*- coding:utf-8 -*-
import sys
import os

import pymysql
import wx
from PyQt5 import QtCore, QtWidgets
from line_profiler_pycharm import profile

import table
import student


@profile
def use():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()  # 创建窗体对象
    ui = table.Ui_MainWindow()  # 创建PyQt设计的窗体对象
    ui.setupUi(MainWindow)  # 调用PyQt窗体的方法对窗体对象进行初始化设置
    MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)  # 只显示关闭按钮
    MainWindow.show()  # 显示窗体
    sys.exit(app.exec_())


@profile
def student_use():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()  # 创建窗体对象
    ui = student.Ui_MainWindow()  # 创建PyQt设计的窗体对象
    ui.setupUi(MainWindow)  # 调用PyQt窗体的方法对窗体对象进行初始化设置
    # MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)  # 只显示关闭按钮
    MainWindow.show()  # 显示窗体
    sys.exit(app.exec_())


class MyFrame(wx.Frame):
    @profile
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, '用户登录', size=(400, 300))
        # 创建面板
        panel = wx.Panel(self)

        # 创建“确定”和“取消”按钮,并绑定事件
        self.bt_confirm = wx.Button(panel, label='确定')
        self.bt_confirm.Bind(wx.EVT_BUTTON, self.OnclickSubmit)
        self.bt_cancel = wx.Button(panel, label='取消')
        self.bt_cancel.Bind(wx.EVT_BUTTON, self.OnclickCancel)
        # 创建文本，左对齐
        self.title = wx.StaticText(panel, label="请输入用户名和密码")
        self.label_user = wx.StaticText(panel, label="学生姓名+空格+性别或”教师“:")
        self.text_user = wx.TextCtrl(panel, style=wx.TE_LEFT)
        self.label_pwd = wx.StaticText(panel, label="密   码:")
        self.text_password = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        # 添加容器，容器中控件按横向并排排列
        hsizer_user = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_user.Add(self.label_user, proportion=0, flag=wx.ALL, border=5)
        hsizer_user.Add(self.text_user, proportion=1, flag=wx.ALL, border=5)
        hsizer_pwd = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_pwd.Add(self.label_pwd, proportion=0, flag=wx.ALL, border=5)
        hsizer_pwd.Add(self.text_password, proportion=1, flag=wx.ALL, border=5)
        hsizer_button = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button.Add(self.bt_confirm, proportion=0, flag=wx.ALIGN_CENTER, border=5)
        hsizer_button.Add(self.bt_cancel, proportion=0, flag=wx.ALIGN_CENTER, border=5)
        # 添加容器，容器中控件按纵向并排排列
        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(self.title, proportion=0, flag=wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER,
                       border=15)
        vsizer_all.Add(hsizer_user, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=45)
        vsizer_all.Add(hsizer_pwd, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=45)
        vsizer_all.Add(hsizer_button, proportion=0, flag=wx.ALIGN_CENTER | wx.TOP, border=15)
        panel.SetSizer(vsizer_all)

    @profile
    def OnclickSubmit(self, event):
        """ 点击确定按钮，执行方法 """
        host = "localhost"
        port = 3306
        user = "root"
        password = "20080928"
        db = "user"
        charset = "utf8"

        db = pymysql.Connect(host=host, port=port, user=user, passwd=password, db=db, charset=charset)
        cursor = db.cursor()

        # global username
        # global password
        username = self.text_user.GetValue()  # 获取输入的用户名
        password = self.text_password.GetValue()  # 获取输入的密码
        sql = "SELECT * FROM stu WHERE names='" + username + "' and passwd = '" + password + "' "
        cursor.execute(sql)
        data = cursor.fetchall()
        # print(data)

        if username == "" or password == "":  # 判断用户名或密码是否为空
            message1 = '用户名或密码不能为空'
            wx.MessageBox(message1)
        elif data is not None and data != ():  # 用户名和密码正确
            message2 = '登录成功'
            path = os.getcwd()
            full_path = path + 'a.txt'
            with open('a.txt', 'w+', encoding='UTF-8') as f:
                f.write(f'{username}\n{password}')

            wx.MessageBox(message2)
            student_use()
        elif username == "教师" and password == "123456":
            wx.MessageBox('登录成功')
            use()
            # return [username, password]
        elif data == ():
            message3 = '用户名和密码不匹配'  # 用户名或密码错误
            wx.MessageBox(message3)  # 弹出提示框

        cursor.close()
        db.close()

    @profile
    def OnclickCancel(self, event):
        """ 点击取消按钮，执行方法 """
        self.text_user.SetValue("")  # 清空输入的用户名
        self.text_password.SetValue("")  # 清空输入的密码


if __name__ == '__main__':
    app = wx.App()  # 初始化
    frame = MyFrame(parent=None, id=-1)  # 实例MyFrame类，并传递参数
    frame.Show()  # 显示窗口
    app.MainLoop()  # 调用主循环方法
