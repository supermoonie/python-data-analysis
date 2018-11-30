import pandas as pda
import pymysql

conn = pymysql.connect(host= '127.0.0.1', port= 3306, user= 'root', password= 'wangchao123', db= 'spider')
sql = 'select * from pianke_user;'
user_data = pda.io.sql.read_sql(sql, conn)
print(user_data.describe())