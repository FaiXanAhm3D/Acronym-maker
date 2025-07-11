import mysql.connector as msc
conn = msc.connect(host='localhost',user='root',password='faizan@sql',database='python')
cursor = conn.cursor()
code = int(input("Enter code: "))
pob = input("Enter new place of birth: ")
query = f"update people set POB = '{pob}' where code={code}"
#query = "update people set pob = {} where code = {}".format(pob,code)
cursor.execute(query)
conn.commit()
if cursor.rowcount > 0: #cursor would have the value of number of row affected by the query
    print(">>>DATA UPDATION COMPLETE<<<")
else:
    print(">NO DATA FOUND<")
