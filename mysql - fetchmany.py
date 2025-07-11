import mysql.connector
conn=mysql.connector.connect(host="localhost",user='root',password="faizan@sql",database='python')
cursor=conn.cursor()
cursor.execute("select * from people")
data=cursor.fetchmany(10)
for i in data:
    print(i)
print("No. of rows --> ",cursor.rowcount)
