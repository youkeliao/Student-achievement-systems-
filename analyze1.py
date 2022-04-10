import pymysql
from decimal import Decimal
from pyecharts.charts import Bar
from pyecharts import options as opts

import model


def students_data():
    host = "localhost"
    port = 3306
    user = "root"
    password = "20080928"
    db = "user"
    charset = "utf8"

    db = pymysql.Connect(host=host, port=port, user=user, passwd=password, db=db, charset=charset)
    cursor = db.cursor()
    sql = "SELECT AVG(total) FROM stu"
    cursor.execute(sql)
    data = cursor.fetchone()
    a = data[0]
    num = Decimal(a).quantize(Decimal("0.1"), rounding="ROUND_HALF_UP")
    num = float(num)
    # print(type(num))
    # 结果：527.3

    sql2 = "SELECT total FROM stu"
    cursor.execute(sql2)
    result = cursor.fetchall()
    result2 = list(result)
    total0 = []
    for i in range(0, 98):
        total0.append(int(result2[i][0]))
    total = [n for n in total0 if n >= num]
    # print(total)  # 及格的分
    sql3 = f"SELECT * FROM stu WHERE total>= {num}"
    cursor.execute(sql3)
    result3 = cursor.fetchall()
    result3 = list(result3)
    # print(len(result3))
    names = []
    for i in range(0, len(result3)):
        names.append(str(result3[i][1]))
    # print(result3)
    # print(names)
    bar = Bar()
    bar.add_xaxis(names)  # 横轴
    bar.add_yaxis("分数", total)  # 纵轴
    bar.set_global_opts(title_opts=opts.TitleOpts(title="达到平均分的学生情况"))
    bar.render("达到平均分的学生情况.html")
    # sql4 = "SELECT * FROM stu排名"
    # cursor.execute(sql4)
    # data2 = list(cursor.fetchall())
    # students = []
    # for i in range(0, len(data2)):
    #     students.append(data2[i][0:12])
    # for j in students:
    #     print("顺序：座号，姓名，语数英政史地物化生")
    #     print(j)

    # print(students)

    cursor.close()
    db.close()
    return num


def students_complete():
    pass


if __name__ == '__main__':
    students_data()
