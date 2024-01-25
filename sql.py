import sqlite3

## Connect to sqlite
connection = sqlite3.connect("student.db")

## Create  a cursor object to insert recond, create table, retrieve (basically do anything)
cursor = connection.cursor()

## create the  table
table_info="""
Create table STUDENT(NAME VARCHAR(25),
                     CLASS VARCHAR(25),
                     SECTION VARCHAR(25),
                     MARKS INT);

"""

cursor.execute(table_info)

## Insert Some more records

cursor.execute('''INSERT INTO STUDENT VALUES('himanshu','Data Science','A',90) ''')
cursor.execute('''INSERT INTO STUDENT VALUES('himanshu','Full stack development ','A',90) ''')
cursor.execute('''Insert Into STUDENT values('Rahul','AI','B',100)''')
cursor.execute('''Insert Into STUDENT values('jayesh','ML','A',86)''')
cursor.execute('''Insert Into STUDENT values('chai','deep learning','A',100)''')
cursor.execute('''Insert Into STUDENT values('sid','AI','A',35)''')
cursor.execute('''Insert Into STUDENT values('Sameep','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('puran','ML','A',35)''')


## display all the records
print("The inssrted records are")

data=cursor.execute('''SELECT * FROM STUDENT''')

for row in data:
    print(row)

## close the connection    

connection.commit()
connection.close()   