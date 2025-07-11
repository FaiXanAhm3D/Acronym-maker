#for more than 1 data insertion
import mysql.connector as msc
conn=msc.connect(host='localhost',user='root',password='faizan@sql',database='python')
cursor=conn.cursor()
while True:
    name = input("Enter name: ")
    code = int(input("Enter code: "))
    pob = input("Enter place of birth: ")
    query = f"insert into people values('{name}',{code},'{pob}')"
    cursor.execute(query)
    conn.commit()
    print(">>>DATA INSERTION COMPLETE<<<")
    a=int(input("Enter 1 --> add more\nEnter 2 --> quit\nEnter your choice: "))
    if a == 2:
        break
    
