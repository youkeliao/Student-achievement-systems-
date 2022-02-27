import time
import os
# from line_profiler_pycharm import profile
import analyze1
import analyze2
import login


# @profile
def teachers_analyze():
    print("数据正在生成，请稍后")
    time.sleep(2)
    login.login_teachers()
    time.sleep(1)
    print("即将打开分析文件...")
    analyze1.students_data()
    time.sleep(0.5)
    os.startfile(os.getcwd()+r"\达到平均分的学生情况.html")
    time.sleep(0.5)
    analyze2.students_pie()
    os.startfile(os.getcwd()+r"\学生情况.html")
    time.sleep(0.8)
    analyze2.students_radar()
    os.startfile(os.getcwd()+r"\平均vs顶尖.html")
    input()


# @profile
def students_analyze():
    print("数据正在生成，请稍后...")
    time.sleep(2)
    analyze2.students_self(login.login_students())
    time.sleep(1)
    os.startfile(os.getcwd()+r"\你的水平vs顶尖水平.html")
    input()


def choice():
    a = input("你是学生还是教师，学生请按1，教师请按2")
    if a == "1":
        students_analyze()
    elif a == "2":
        teachers_analyze()
    else:
        print("请重新输入")
        choice()


choice()
