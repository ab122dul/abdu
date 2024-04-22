#project 5 using XAMPP.

'''import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    dataabase="Customers"
)
mycursor= mydb.cursor()

mycursor.execute("create database mydatabase")
print("Dsatabase created successfully.")

mycursor.execute("Create table mytable(name varchar(120),age varchar(2),address varchar(120),cont_per varchar(120))")
print("Data table create successfully.")

sql= " insert into mytable(name,age,address,cont_per) values(%s,%s,%s,%s)"
val=("Mr.Dhoni","44","Ranchi","Mr.Dewan")
mycursor.execute(sql,val)
mydb.commit()
print("Data inserted successfully.")

val=[
    ("Mrs.Dey","64", "kolkata","Mr.Dey"),
    ("Mr.Kanjilal","44","Bangalore","Mr.Das"),
    ("Mrs.Kumar","39","Delhi","Mrs .Kumar")
]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"has inserted")

mycursor=mydb.cursol()
sql="select * from mytable where name ='Mrs.Dey'"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for n in myresult:
    print(n)'''

#Project-6 : Employee Management:-

import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Emp_Man"
)    
mycursor=mydb.cursor()

'''mycursor.execute("create database Emp_Man")
print("Database created successsfully.")
'''
'''mycursor.execute("create table emp_table(id int(2) primary key auto_increment,name varchar(120),address varchar(120),phone varchar(10),main varchar(100),department varchar(100))")
print("Table crated  successfully.")'''

sql="insert into emp_table(id,name,address,phone,main,department) values(%s,%s,%s,%s,%s,%s)"
val=[
('',"Mr.Das","Kolkata","621922810","das220@gmail.com","Sales"),
('',"Mrs.Adhikari","darjeeling","72990107771","adhi22@gmail.com","Accounts"),
('',"Mr.sen","Kurseong","1933662219","sen221@gamill.com","Purchaes")    
]
'''mycursor.executemany(sql,val)
mydb.commit()
print(mycursor._rowcount,"row/s inserted.")'''

'''sql="select *from emp_table"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for u in myresult:
    print(u)'''
    
sql="update emp_table set name=%s where name =%s"
val=("Mrs.Das","mr.Das")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"row/s affected")
    