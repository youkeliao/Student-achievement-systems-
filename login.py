import pymysql


def get_data(sql):
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

    cursor.close()
    db.close()

    return data


def get_data2(sql):
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

    return data


def login_students():
    username = input('请输入学生名字加上空格然后性别（如：张三 男）：')
    user_password = input('请输入密码：')
    sql = "SELECT * FROM stu WHERE names='" + username + "' and passwd = '" + user_password + "' "
    data = get_data2(sql)
    if data is None:
        print("请重新输入")
        login_students()
    else:
        print("登录成功，学生信息为：", data[0][1], "排序规则：座号姓名语数英政史地物化生总分密码")
        for i in range(0, len(data)):
            result09 = list(list(data[0]))[2:11]
            result = []
            for i in range(0, len(result09)):
                result.append(int(result09[i]))
            # print(result)
            return result


def login_teachers():
    password = input("请输入教师密码")  # 123456
    sql2 = "SELECT * FROM stu排名"
    data2 = get_data2(sql=sql2)
    if password == "123456":
        for i in data2:
            print("顺序：座号  名字  语文  数学  英语  政治  历史  地理  物理  化学  生物  总分")
            print("登录成功，学生排名从上到下依次为：", i[0:12])
        return 1

    else:
        print("请重新输入")
        login_teachers()


def students_teachers():
    user_type = input("你是学生还是教师，学生请输入1，教师请输入2")
    if user_type == "1":
        login_students()
        return 0
    elif user_type == "2":
        login_teachers()
        return 1
    else:
        print("请重新输入")
        students_teachers()


if __name__ == '__main__':
    students_teachers()
    print(login_students())
    input()
