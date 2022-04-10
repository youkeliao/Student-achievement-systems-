# 基础模块，底层模块，不要乱动
from decimal import Decimal
import pymysql

subject0 = ["语文", "数学", "英语", "政治", "历史", "地理", "物理", "化学", "生物"]


def sql_select(sql):
    host = "localhost"
    port = 3306
    user = "root"
    password = "20080928"
    db = "user"
    charset = "utf8"

    db = pymysql.Connect(host=host, port=port, user=user, passwd=password, db=db, charset=charset)
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchone()
    # print(data)
    cursor.close()
    db.close()
    return data


def sql_select2(sql):
    host = "localhost"
    port = 3306
    user = "root"
    password = "20080928"
    db = "user"
    charset = "utf8"

    db = pymysql.Connect(host=host, port=port, user=user, passwd=password, db=db, charset=charset)
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()

    cursor.close()
    db.close()

    # print(data)
    return data


def average(subject):
    sql = f"SELECT AVG({subject}) FROM stu"
    # print(sql)
    num = sql_select(sql)[0]
    num = Decimal(num).quantize(Decimal("0.1"), rounding="ROUND_HALF_UP")
    num = float(num)
    return num


Chinese = average("Chinese")
math = average("math")
English = average("English")
political = average("political")
history = average("history")
geography = average("geography")
physics = average("physics")
chemistry = average("chemistry")
biology = average("biology")


def tops(y):
    sql = "SELECT total FROM stu排名"
    result = list(sql_select2(sql))
    num = [list(row) for row in result]
    top = [int(x) for item in num for x in item]
    your_top = top.index(y) + 1
    return your_top


def good(student):
    sql = f"SELECT * FROM stu WHERE names='{student}'"
    # print(sql)
    data = list(sql_select(sql))
    data = [i for i in data][2:11]
    result0 = []
    for j in range(0, len(data)):
        result0.append(int(data[j]))

    subjects = [Chinese, math, English, political, history, geography, physics, chemistry, biology]
    result = [result0[v] for v in range(0, len(subjects)) if result0[v] > subjects[v] * 1.5]
    # for v in range(0, len(subject)):
    #     if result0[v] > subject[v]:
    #         print(result0[v])
    dict1 = dict(zip(result0, subject0))
    best = [dict1[result[d]] for d in range(0, len(result))]
    # print(result)
    return best


def bad(student):
    sql = f"SELECT * FROM stu WHERE names='{student}'"
    # print(sql)
    data = list(sql_select(sql))
    data = [i for i in data][2:11]
    result0 = []
    for j in range(0, len(data)):
        result0.append(int(data[j]))

    subjects = [Chinese, math, English, political, history, geography, physics, chemistry, biology]
    result = [result0[v] for v in range(0, len(subjects)) if result0[v] < subjects[v] or result0[v] < 60]
    # for v in range(0, len(subject)):
    #     if result0[v] > subject[v]:
    #         print(result0[v])
    dict1 = dict(zip(result0, subject0))
    list1 = [dict1[result[d]] for d in range(0, len(result))]
    # print(result)
    return list1


def percent(student, config):
    """
    config = 0返回得分率，1返回总分
    """
    sql = f"SELECT total FROM stu WHERE names = '{student}'"
    data = sql_select(sql)
    data = int(data[0])
    result = data / 1050
    x = Decimal(result).quantize(Decimal("0.01"), rounding="ROUND_HALF_UP")
    num = float(x) * 100
    if config == 0:
        print(num)
        return num
    elif config == 1:
        return data


if __name__ == '__main__':
    print(good("韩琬 女"))
    print(bad("韩琬 女"))
    print(percent("衡智松 男", config=0))
    print(tops(percent("韩琬 女", config=1)))
    # print(tops(753))
    # print(average(subject="Chinese"))
