import pymysql

db_settings = {
    "host": "localhost",
    "port": 3306,
    "user": "sqluser",
    "password": "0310",
    "db": "test1",
    "charset": "utf8"
}
# 打开数据库连線
conn = pymysql.connect(**db_settings)
cursor = conn.cursor()#建立cursor物件

# 创建資料表
# sqldata = """CREATE TABLE student1 (
#          id  INTEGER PRIMARY KEY NOT NULL,
#          name  VARCHAR(20),
#          age INTEGER,  
#          Birthday DATE)"""

# cursor.execute(sqldata)
# 刪除資料表
# cursor.execute('DROP TABLE `student`')

# datatable = """INSERT INTO `student1` VALUES(4,"小綠",23,'2000-12-20');"""
# cursor.execute(datatable)
#新增資料

# 資料查詢

cursor.execute('select * from `student1`;')
rows = cursor.fetchall()

for row in rows:
    print(row[0],row[1],row[2],row[3])#顯示欄位

conn.commit()
conn.close()