import traceback
import sys
import mysql.connector as msc
import faker

fake=faker.Faker()

def table_function(db_name):
    print('''>>> SELECT THE FUNCTION IN BRACKET <<<
To SHOW list of tables-------(Show)
To SELECT data from a table--(Select)
To CREATE a table------------(Create)
To INSERT data into a table--(Insert)
To DROP a table--------------(Drop)
To DELETE data from a table--(Delete)
To UPDATE a table------------(Update)
To ALTER data of a table-----(Alter)
To get structure of a table--(Desc)
To go BACK-------------------(Back)
To quit----------------------(Quit) or (Exit) or (Stop) or (Esc)''')
    
    function=input("Enter the function: ").lower().strip()
    if function=='back':
        Open()
    elif function in ['quit','exit','stop','esc']:
        quit()
    elif function=='show':
        table_list(db_name)
    elif function=='create':
        table_create(db_name)
    elif function=='drop':
        table_drop(db_name)
    elif function=='select':
        table_select(db_name)
    elif function=='insert':
        table_insert(db_name)
    elif function=='delete':
        table_delete(db_name)
    elif function=='update':
        table_update(db_name)
    elif function=='desc':
        table_desc(db_name)
    elif function=='alter':
        table_alter(db_name)
    else:
        print(">>> INVALID INPUT <<<",'\n')
        table_function(db_name)

def table_alter(db_name):
    print('>')
    print("To go BACK (Back)")
    print('''>>> SELECT THE ALTER FUNCTION <<<
ADD COLUMN-----(ADD)
DROP COLUMN----(DROP)
RENAME COLUMN--(RENAME)
MODIFY COLUMN--(MODIFY)
RENAME TABLE---(TABLE)''')
    alter_func=input("Enter the function: ").lower().strip()
    try:
        name=input("Enter the NAME of the table: ").lower().strip()
        if name=='back':
            table_function()
        else:
            connection=msc.connect(host='localhost',
                                   user='root',
                                   password='faizan@sql',
                                   database=f'{db_name}')
            mycursor=connection.cursor()
        if alter_func=='add':
            column_name=input("Enter column name: ")
            column_type=input("Enter data type: ")
            column_constraint=input("Enter constraints separated by space (if any, skip otherwise): ")
            query=f'ALTER TABLE {name} ADD COLUMN {column_name} {column_type} {column_constraint}'
            print(query)
            mycursor.execute(query)
            print(">>> TABLE ALTERED SUCCESFULLY <<<")
            connection.commit()
            print('>')
            table_function(db_name)
        elif alter_func=='drop':
            column_name=input("Enter column name: ")
            query=f'ALTER TABLE {name} DROP COLUMN {column_name}'
            print(query)
            mycursor.execute(query)
            print(">>> TABLE ALTERED SUCCESFULLY <<<")
            connection.commit()
            print('>')
            table_function(db_name)
        elif alter_func=='rename':
            column_oname=input("Enter previous column name: ")
            column_nname=input("Enter new column name: ")
            column_datatype=input("Enter data type: ")
            column_constraint=input("Enter constraints(if any, skip otherwise): ")
            query=f'ALTER TABLE {name} CHANGE {column_oname} {column_nname} {column_datatype} {column_constraint}'
            print(query)
            mycursor.execute(query)
            print(">>> TABLE ALTERED SUCCESFULLY <<<")
            connection.commit()
            print('>')
            table_function(db_name)
        elif alter_func=='modify':
            column_name=input("Enter column name: ")
            column_datatype=input("Enter new data type: ")
            column_constraint=input("Enter constraints(if any, skip otherwise): ")
            query=f'ALTER TABLE {name} MODIFY {column_name} {column_datatype} {column_constraint}'
            print(query)
            mycursor.execute(query)
            print(">>> TABLE ALTERED SUCCESFULLY <<<")
            connection.commit()
            print('>')
            table_function(db_name)
        elif alter_func=='table':
            table_name=input("Enter name of the table: ")
            new_table_name=input("Enter new table name: ")
            query=(f'ALTER TABLE {table_name} RENAME TO {new_table_name}')
            print(query)
            mycursor.execute(query)
            print(">>> TABLE ALTERED SUCCESFULLY <<<")
            connection.commit()
            print('>')
            table_function(db_name)
            
    except Exception as e:
        print("An error occurred:", e)
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print("Error occurred on line:", exc_traceback.tb_lineno)
        print('>')
        table_function(db_name)
        
def table_desc(db_name):
    print('>')
    print("To go BACK (Back)")
    try:
        name=input("Enter the NAME of the table: ").lower().strip()
        if name=='back':
            table_function()
        else:
            connection=msc.connect(host='localhost',
                                   user='root',
                                   password='faizan@sql',
                                   database=f'{db_name}')
            mycursor=connection.cursor()
            mycursor.execute(f"DESCRIBE {name}")
            column_names = mycursor.column_names
            for i in column_names:
                print(i,end= ' ')
            print('\n')
            for i in mycursor:
                for j in i:
                    print(j,end=' ')
                print('\n')
            print('>')
            table_function(db_name)
            
    except Exception as e:
        print("An error occurred:", e)
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print("Error occurred on line:", exc_traceback.tb_lineno)
        print('>')
        table_function(db_name)

def table_update(db_name):
    print('>')
    print("To go BACK (Back)")
    try:
        name=input("Enter the NAME of the table: ").lower().strip()
        if name=='back':
            table_function()
        column=input("Enter the NAME of the column: ").lower().strip()
        if column=='back':
            table_function()
        new_data=input("Enter the NEW DATA: ").strip()
        if new_data.lower()=='back':
            table_function()
        where=input("Enter CONDITION(WHERE CLAUSE--\nWHERE ").lower().strip()
        if where=='back':
            table_function()
        connection=msc.connect(host='localhost',
                                   user='root',
                                   password='faizan@sql',
                                   database=f'{db_name}')
        mycursor=connection.cursor()
        query=f"UPDATE {name} SET {column} = {new_data} WHERE {where}"
        print(query)
        mycursor.execute(query)
        print(">>> DATA UPDATED SUCCESFULLY <<<")
        connection.commit()
        print('>')
        table_function(db_name)
        
    except Exception as e:
        print("An error occurred:", e)
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print("Error occurred on line:", exc_traceback.tb_lineno)
        print('>')
        table_function(db_name)

def table_delete(db_name):
    print('>')
    print("To go BACK (Back)")
    try:
        name=input("Enter the NAME of the table: ").lower().strip()
        if name=='back':
            table_function()
        connection=msc.connect(host='localhost',
                                   user='root',
                                   password='faizan@sql',
                                   database=f'{db_name}')
        mycursor=connection.cursor()
        where=input('''Enter CONDITION(WHERE CLAUSE) to delete data--
WHERE ''')
        if where.lower()=='back':
            table_function()
        query=f"DELETE FROM {name} WHERE {where}"
        print(query)
        mycursor.execute(query)
        print(">>> DATA DELETED SUCCESFULLY <<<")
        connection.commit()
        print('>')
        table_function(db_name)
        
    except Exception as e:
        print("An error occurred:", e)
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print("Error occurred on line:", exc_traceback.tb_lineno)
        print('>')
        table_function(db_name)

def table_select(db_name):
    print('>')
    print("To go BACK (Back)")
    try:
        connection=msc.connect(host='localhost',
                                   user='root',
                                   password='faizan@sql',
                                   database=f'{db_name}')
        mycursor=connection.cursor()
        select=input("Enter the NAME(s) of column--\nSELECT ").lower().strip()
        if select=='back':
            table_function(db_name)
        From=input("Enter the NAME of the table--\nFROM ").lower().strip()
        if From=='back':
            table_function(db_name)
        join=input("Enter table NAME to join (if any, skip otherwise)--\nJOIN ").lower().strip()
        if join=='back':
            table_function(db_name)
        on=input("Enter the common COLUMN (if any, skip otherwise)--\nON ").lower().strip()
        if on=='back':
            table_function(db_name)
        where=input("Enter WHERE CLAUSE (if any, skip otherwise)--\nWHERE ").strip()
        if where=='back':
            table_function(db_name)
        group_by=input("Enter GROUP BY CLAUSE (if any, skip otherwise)--\nGROUP BY ").lower().strip()
        if group_by=='back':
            table_function(db_name)
        having=input("Enter HAVING CLAUSE (if any, skip otherwise)--\nHAVING ").strip()
        if having=='back':
            table_function(db_name)
        order=input("Enter ORDER BY CLAUSE (if any, skip otherwise)--\nORDER BY ").lower().strip()
        if order=='back':
            table_function(db_name)
        limit=input("Enter LIMIT (if any, skip otherwise)--\nLIMIT ").lower().strip()
        if limit=='back':
            table_function(db_name)

        query="SELECT "+select+' '+"FROM "+' '+From
        if join:
            query=query+' '+'JOIN'+' '+join
        if on:
            query=query+' '+'ON'+' '+on
        if where:
            query=query+' '+'WHERE'+' '+where
        if group_by:
            query=query+' '+'GROUP BY'+' '+group_by
        if having:
            query=query+' '+'HAVING'+' '+having
        if order:
            query=query+' '+'ORDER BY'+' '+order
        if limit:
            query=query+' '+'LIMIT'+' '+limit
        print('>')
        print(query)
        mycursor.execute(query)
        column_names = mycursor.column_names
        print('> ',column_names)
        lst=[]
        for i in mycursor:
            lst.append(i)
        for i in lst:
            print('> ',i)
        print('>')
        table_function(db_name)
        
    except Exception as e:
        print("An error occurred:", e)
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print("Error occurred on line:", exc_traceback.tb_lineno)
        print('>')
        table_function(db_name)

def table_insert(db_name):
    print('>')
    print("To go BACK (Rollback)")
    name=input("Enter NAME of the table: ").lower().strip()
    if name=='rollback':
            table_function(db_name)
    number=int(input("Enter NUMBER of data(or tuples): "))
    try:
        connection=msc.connect(host='localhost',
                                   user='root',
                                   password='faizan@sql',
                                   database=f'{db_name}')
        mycursor=connection.cursor()
        mycursor.execute(f"SELECT * FROM {name}")#some issues regarding cursor placement :/
        column_name=mycursor.column_names
        mycursor.fetchall()#some issues regarding unread result :/
        #print(column_name)
        for i in range(number):
            lst = []
            for j in column_name:
                #print("loop of j")
                data = input(f"Enter {j}: ")
                if data=='rollback':
                    table_function(db_name)
                else:
                    lst.append(data)
            #print(lst)
            final_data=",".join(lst)
            query = f'INSERT INTO {name} VALUES ({final_data})'
            print(query)
            mycursor.execute(query)
            connection.commit()
        print(">>> DATA INSERTED SUCCESFULLY <<<")
        print('>')
        table_function(db_name)
        connection.close()
            
    except Exception as e:
        print("An error occurred:", e)
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print("Error occurred on line:", exc_traceback.tb_lineno)
        print('>')
        table_function(db_name)
       
def table_drop(db_name):
    print('>')
    print("To go BACK (Back)")
    try:
        table_name=input("Enter the NAME of the table: ").lower().strip()
        if table_name=='back':
            table_function(db_name)
        connection=msc.connect(host='localhost',
                                   user='root',
                                   password='faizan@sql',
                                   database=f'{db_name}')
        mycursor=connection.cursor()
        mycursor.execute(f"DROP TABLE {table_name}")
        print(">>> TABLE DELETED SUCCESFULL <<<")
        connection.commit()
        print('>')
        table_function(db_name)

    except Exception as e:
        print("An error occurred:", e)
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print("Error occurred on line:", exc_traceback.tb_lineno)
        print('>')
        table_function(db_name)

def table_create(db_name):
    print('>')
    print("To go BACK (Back)")
    try:
        connection=msc.connect(host='localhost',
                                   user='root',
                                   password='faizan@sql',
                                   database=f'{db_name}')
        mycursor=connection.cursor()
        table_name=input("Enter NAME of the table: ")
        if table_name=='back':
            table_function()
        lst=[]
        column=int(input("Enter NUMBER of columns: "))
        for i in range(column):
            desc_column=input("Enter NAME of column, DATA TYPE and CONSTRAINTS (separated by space)\nEnter: ")
            if desc_column=='back':
                table_function()
            lst.append(desc_column)
        table_schema = ', '.join(lst)#The join() method takes all items in an iterable and
                                     #joins them into one string and a string must be
                                     #specified as the separator. 
        #print(table_schema)
        mycursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name}({table_schema})")
        print(">>> TABLE CREATION SUCCESFULL <<<")
        connection.commit()
        print('>')
        table_function(db_name)

    except Exception as e:
        print("An error occurred:", e)
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print("Error occurred on line:", exc_traceback.tb_lineno)
        print('>')
        table_function(db_name)

def table_list(db_name):
    print('>')
    try:
        connection=msc.connect(host='localhost',
                                   user='root',
                                   password='faizan@sql',
                                   database=f'{db_name}')
        mycursor=connection.cursor()
        mycursor.execute("SHOW TABLES")
        lst=[]
        for i in mycursor:
            dat=', '.join(i)
            lst.append(dat)
        if lst==[]:
            print(">>> EMPTY <<<")
            print('>')
            table_function(db_name)
        else:
            for i in lst:
                print('> ',i)
            print('>')
            table_function(db_name)

    except Exception as e:
        print("An error occurred:", e)
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print("Error occurred on line:", exc_traceback.tb_lineno)
        print('>')
        table_function(db_name)

def show():
    try:
        connection=msc.connect(host='localhost',
                           user='root',
                           password='faizan@sql')
        mycursor=connection.cursor()
        mycursor.execute("SHOW DATABASES")
        lst=[]
        for i in mycursor:
            dat=', '.join(i)
            lst.append(dat)
        for i in lst:
            print('> ',i)
        print('>')
        front_end()
        
    except Exception as e:
        print("An error occurred:", e)
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print("Error occurred on line:", exc_traceback.tb_lineno)
        print('>')
        show()
    
def Open():
    print("To go BACK enter Back or")
    try:
        db_name=input('''Select the NAME of database
Enter: ''')
        if db_name.lower().strip()=='back':
            print('>')
            front_end()
        else:
            connection=msc.connect(host='localhost',
                               user='root',
                               password='faizan@sql',
                               database=f'{db_name}')
            mycursor=connection.cursor()
            if connection.is_connected():
                print(f">>> DATABASE {db_name} IS SELECTED <<<")
                print('>')
                table_function(db_name)
            else:
                print(">>> FAILED TO CONNECT TO DATABASE <<<")
                print('>')
                Open()
        
    except Exception as e:
        print("An error occurred:", e)
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print("Error occurred on line:", exc_traceback.tb_lineno)
        print('>')
        Open()

def create():
    print("To go BACK enter Back or")
    try:
        db_name=input('''Enter the NAME of database
Enter: ''')
        if db_name.lower().strip()=='back':
            print('\n')
            front_end()
        else:
            connection=msc.connect(host='localhost',
                               username='root',
                               password='faizan@sql')
            cursor=connection.cursor()
            cursor.execute(f"CREATE DATABASE {db_name}")
            print(">>> DATABASE CREATED SUCCESFULLY <<<")
            print('\n')
            front_end()
            
    except Exception as e:
        print("An error occurred:", e)
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print("Error occurred on line:", exc_traceback.tb_lineno)
        print('>')
        create()

def drop():
    try:
        db_name=input('''Enter the NAME of database or To go BACK(Back)
Enter: ''')
        if db_name.lower().strip()=='back':
            print('\n')
            front_end()
        else:
            connection=msc.connect(host='localhost',
                               user='root',
                               password='faizan@sql')
            mycursor=connection.cursor()
            mycursor.execute(f"DROP DATABASE {db_name}")
            print(">>> DATABASE DELETED SUCCESFULLY <<<")
            print('\n')
            front_end()
    except Exception as e:
        print("An error occurred:", e)
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print("Error occurred on line:", exc_traceback.tb_lineno)
        print('>')
        drop()

def front_end():
    print('''>>> SELECT THE FUNCTION IN BRACKET <<<

To SHOW the list of databases--(Show)
To USE a database--------------(Use)
To CREATE a database-----------(Create)
To DROP a database-------------(Drop)
To quit------------------------(Quit) or (Exit) or (Stop) or (Esc)''')
    
    function=input("Enter the function: ").lower().strip()
    if function=='show':
        print('>')
        show()
    elif function=='use':
        print('>')
        Open()
    elif function=='create':
        print('>')
        create()
    elif function=='drop':
        print('>')
        drop()
    elif function in ['quit','exit','stop','esc']:
        quit()
    else:
        print(">>> INVALID INPUT <<<",'\n')
        front_end()

front_end()
    
    
