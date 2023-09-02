import mysql.connector # pip install mysql-connector-python

connect = mysql.connector.connect(host="localhost", port="3306", user="root", passwd="", database="grafikuczelni")

cursor = connect.cursor()
query = "select * from pracownicy"
cursor.execute(query)
records = cursor.fetchall()

for i in range(len(records)):
    print(records[i])