import mysql.connector

conn = mysql.connector.connect(host = 'localhost',user='root',password='1432',database='snk1')

mycursor = conn.cursor()

sql = 'insert into student (name,branch,id) values(%s,%s,%s)'
#val = ('john','cse',56)

# if user want to create multiple value then you can creat list 
val = [('Sangamesh','cse','56'),('swaraj','IT','78'),('vishwaradhya','me','80')]
#mycursor.execute(sql,val)
mycursor.executemany(sql,val)
conn.commit()
print(mycursor.rowcount,'record inserted')