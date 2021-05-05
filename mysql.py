"""编程的思想解决数据库SQL操作"""
# https://www.bilibili.com/video/BV1vi4y137PN?p=27

import pymysql

try:
    # 连接服务
    coonc = pymysql.connect(
        # host='127.0.0.1',
        user='root',
        password='123456',
        database='test',
        port=3306,
        charset='utf8'
    )

    # 创建游标
    cursor = coonc.cursor()

    # #查
    # sql = 'select * from student where score<=50;'
    # cursor.execute(sql)

    # #增
    # sql = 'insert into student values(12,"lxl0d",45,"male");'
    # cursor.execute(sql)

    # # 增
    # sql = 'insert into student values(%s,%s,%s,%s);'
    # dataset = [12, "lxl30d", 45, "male"]
    # cursor.execute(sql, dataset)

    # # 改
    # sql = 'update student set score=40 where id=5;'
    # cursor.execute(sql)

    # #删
    sql = 'delete from student where name=%s;'
    dataset=["xiaoping"]
    # 使用游标对象执行SQL操作
    cursor.execute(sql,dataset)

    # 提交，数据库才会实际改变
    coonc.commit()

    # 查 不需要commit提交
    sql_2 = 'select * from student;'
    cursor.execute(sql_2)
    result = cursor.fetchall()
    res = [result[i] for i in range(len(result))]
    for i in res:
        print(i)

except Exception as e:
    # 打印报错信息
    print(e)
    # 数据回滚，避免失败影响数据
    coonc.rollback()

finally:
    # 关闭游标
    cursor.close()
    # 断开连接
    coonc.close()
    # Over!
    print('数据库操作结束')