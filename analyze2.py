import pymysql
from pymysql.constants import CLIENT
from pyecharts.charts import Pie
from pyecharts.charts import Radar
from pyecharts import options as opts
# from line_profiler_pycharm import profile

# @profile
def students_pie():
    host = "localhost"
    port = 3306
    user = "root"
    password = "20080928"
    db = "user"
    charset = "utf8"

    db = pymysql.Connect(host=host, port=port, user=user, passwd=password, db=db, charset=charset)
    cursor = db.cursor()

    sql = "SELECT names FROM stu WHERE total>=630"  # 及格人数
    sql2 = "SELECT names FROM stu WHERE total<630 AND total>=527.3"
    sql3 = "SELECT names FROM stu WHERE total<527.3"
    cursor.execute(sql)
    data1 = cursor.fetchall()
    cursor.execute(sql2)
    data2 = cursor.fetchall()
    cursor.execute(sql3)
    data3 = cursor.fetchall()
    # print(len(data1))
    # print(len(data2))
    # print(len(data3))
    pie = Pie()
    students_type = ["及格人数", "达到平均分人数", "剩下的渣"]
    total = [len(data1), len(data2), len(data3)]
    data_list = []
    for i in range(0, len(students_type)):
        d = [students_type[i], total[i]]
        data_list.append(d)
    # print(data_list)
    pie.set_global_opts(title_opts=opts.TitleOpts(title="学生情况"))
    pie.add("分", data_list)
    pie.render("学生情况.html")

    cursor.close()
    db.close()


# @profile
def students_radar():

    host = "localhost"
    port = 3306
    user = "root"
    password = "20080928"
    db = "user"
    charset = "utf8"

    db = pymysql.Connect(host=host, port=port, user=user, passwd=password, db=db, charset=charset,
                         client_flag=CLIENT.MULTI_STATEMENTS)
    cursor = db.cursor()
    sql = "SELECT AVG(Chinese) FROM stu"
    cursor.execute(sql)
    data = cursor.fetchone()
    sql2 = "SELECT AVG(math) FROM stu"
    cursor.execute(sql2)
    data2 = cursor.fetchone()
    sql3 = "SELECT AVG(English) FROM stu"
    cursor.execute(sql3)
    data3 = cursor.fetchone()
    sql4 = "SELECT AVG(political) FROM stu"
    cursor.execute(sql4)
    data4 = cursor.fetchone()
    sql5 = "SELECT AVG(history) FROM stu"
    cursor.execute(sql5)
    data5 = cursor.fetchone()
    sql6 = "SELECT AVG(geography) FROM stu"
    cursor.execute(sql6)
    data6 = cursor.fetchone()
    sql7 = "SELECT AVG(physics) FROM stu"
    cursor.execute(sql7)
    data7 = cursor.fetchone()
    sql8 = "SELECT AVG(chemistry) FROM stu"
    cursor.execute(sql8)
    data8 = cursor.fetchone()
    sql9 = "SELECT AVG(biology) FROM stu"
    cursor.execute(sql9)
    data9 = cursor.fetchone()

    avg = [[data[0], data9[0], data8[0], data7[0], data6[0], data5[0], data4[0], data3[0], data2[0]]]
    high = "SELECT * FROM stu排名 limit 0,1"
    cursor.execute(high)
    higher = cursor.fetchone()
    number09 = list(higher)[2:11]
    number1 = []
    for i in range(0, len(number09)):
        number1.append(int(number09[i]))
    # print(number1)
    c = (
        Radar()
            .add_schema(
            schema=[
                opts.RadarIndicatorItem(name="语文", max_=150),
                opts.RadarIndicatorItem(name="数学", max_=150),
                opts.RadarIndicatorItem(name="英语", max_=150),
                opts.RadarIndicatorItem(name="政治", max_=100),
                opts.RadarIndicatorItem(name="历史", max_=100),
                opts.RadarIndicatorItem(name="地理", max_=100),
                opts.RadarIndicatorItem(name="物理", max_=100),
                opts.RadarIndicatorItem(name="化学", max_=100),
                opts.RadarIndicatorItem(name="生物", max_=100)
            ]
        )
            .add("平均水平", avg)
            .add("顶尖水平", [number1])
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            legend_opts=opts.LegendOpts(selected_mode="single"),
            title_opts=opts.TitleOpts(title="分析器"),
        )
            .render("平均vs顶尖.html")
    )

    cursor.close()
    db.close()

def students_self(data=None):
    if data is None:
        data = []

    host = "localhost"
    port = 3306
    user = "root"
    password = "20080928"
    db = "user"
    charset = "utf8"

    db = pymysql.Connect(host=host, port=port, user=user, passwd=password, db=db, charset=charset,
                         client_flag=CLIENT.MULTI_STATEMENTS)
    cursor = db.cursor()
    high = "SELECT * FROM stu排名 limit 0,1"
    cursor.execute(high)
    higher = cursor.fetchone()
    number09 = list(higher)[2:11]
    number1 = []

    for i in range(0, len(number09)):
        number1.append(int(number09[i]))
    c = (
        Radar()
            .add_schema(
            schema=[
                opts.RadarIndicatorItem(name="语文", max_=150),
                opts.RadarIndicatorItem(name="数学", max_=150),
                opts.RadarIndicatorItem(name="英语", max_=150),
                opts.RadarIndicatorItem(name="政治", max_=100),
                opts.RadarIndicatorItem(name="历史", max_=100),
                opts.RadarIndicatorItem(name="地理", max_=100),
                opts.RadarIndicatorItem(name="物理", max_=100),
                opts.RadarIndicatorItem(name="化学", max_=100),
                opts.RadarIndicatorItem(name="生物", max_=100)
            ]
        )
            .add("你的水平", [data])
            .add("顶尖水平", [number1])
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            legend_opts=opts.LegendOpts(selected_mode="single"),
            title_opts=opts.TitleOpts(title="分析器"),
        )
            .render("你的水平vs顶尖水平.html")
    )
    cursor.close()
    db.close()


if __name__ == '__main__':
    students_pie()
    students_radar()


# @profile
# def lab():
#     host = "localhost"
#     port = 3306
#     user = "root"
#     password = "20080928"
#     db = "user"
#     charset = "utf8"
#
#     db = pymysql.Connect(host=host, port=port, user=user, passwd=password, db=db, charset=charset,
#                              client_flag=CLIENT.MULTI_STATEMENTS)
#     cursor = db.cursor()
#
#     high = "SELECT * FROM stu排名 limit 0,1"
#     cursor.execute(high)
#     higher = cursor.fetchone()
#     number09 = list(higher)[2:11]
#     number1 = []
#     for i in range(0, len(number09)):
#         number1.append(int(number09[i]))
#     print(number1)
#     cursor.close()
#     db.close()
# lab()
