import mysql.connector as msc
conn = msc.connect(host='localhost',user='root',password='faizan@sql',database='python')
cursor = conn.cursor()
name = input("Enter name: ")
code = int(input("Enter code: "))
pob = input("Enter place of birth: ")
query = f"insert into people values('{name}',{code},'{pob}')"
cursor.execute(query)
conn.commit()
print("Data insertion successfull")
