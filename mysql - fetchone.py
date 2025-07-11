import mysql.connector as msc
conn=msc.connect(host="localhost",user='root',password='faizan@sql',database='python')
cursor=conn.cursor()
cursor.execute("select * from people")
data=cursor.fetchone()
print(data)
print("Total number of rows retrived -->",cursor.rowcount)
data=cursor.fetchone()
print(data)
print("Total number of rows retrived -->",cursor.rowcount)
data=cursor.fetchone()
print(data)
print("Total number of rows retrived -->",cursor.rowcount)
#rowcount would give the number of rows which is obtained by fetch function
