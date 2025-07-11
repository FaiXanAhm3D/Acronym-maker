import mysql.connector as msc
conn = msc.connect(host='localhost',user='root',password='faizan@sql',database='python')
cursor=conn.cursor()
cursor.execute("Select * from people")
data = cursor.fetchall()
for i in data:
    print(i)

print("Number of rows retrieved -->",cursor.rowcount)
