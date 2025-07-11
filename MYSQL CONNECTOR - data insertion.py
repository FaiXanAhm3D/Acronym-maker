import mysql.connector as msc
connection = msc.connect(host='localhost',user='root',password='faizan@sql',database='python')
cursor = connection.cursor()
name=input("Enter name: ")
code=int(input("Enter code: "))
pob=input("Enter place of birth: ")
query = "insert into people values('{}',{},'{}')".format(name,code,pob)
#query = f"insert into people values('{name}',{code},'{pob}')"
cursor.execute(query)
connection.commit()
print(">>>DATA INSERTION COMPLETED<<<")
