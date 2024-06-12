import pymysql

# 建立数据库连接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='020719',
    db='test_pymysql',
    charset='utf8'
)

# 获取游标
# cursor = conn.cursor()

#每条记录为字典格式
cursor = conn.cursor(pymysql.cursors.DictCursor)

# 执行sql语句
#插入单条语句
# sql = 'insert into test_01(id,name) values(%s,%s)'
# rows = cursor.execute(sql, ('1', 'zhangSan'))

#插入多条语句
# sql = 'insert into test_01(id,name) values(%s,%s)'
# rows = cursor.executemany(sql, [('2', 'lisi'), ('3', 'xiaoWu'), ('4', 'Dada')])

#插入大批量数据
# values = []
# for i in range(100, 201):
#     values.append((i, 'more'+str(i)))
# sql = 'insert into test_01(id,name) values(%s,%s)'
# rows = cursor.executemany(sql, values)

#修改数据
# sql = 'update test_01 set name = %s where id = %s'
# rows = cursor.execute(sql, ('qzcsbj', '1'))

#删除数据
# sql = 'delete from test_01 where id = %s'
# rows = cursor.execute(sql, ('1',))

'''
查询数据
fetchone
有点像从管道中取一个，如果再来一个fetchone，会又取下一个，如果取完了再取，就返回None
'''
rows = cursor.execute('select * from test_01;')
# print(cursor.fetchone())
# print(cursor.fetchone())

#打印结果为字典格式用：fetchmany 函数
# print(cursor.fetchmany(5))

#相对绝对位置移动，从头开始跳过n个
cursor.scroll(3, mode='absolute')
print(cursor.fetchmany(2))

# 提交
conn.commit()

# 关闭游标
cursor.close()

# 关闭连接
conn.close()