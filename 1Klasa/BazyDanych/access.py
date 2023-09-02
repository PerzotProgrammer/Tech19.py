import pyodbc # pip install pyodbc

connect = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\\Users\\pogra\\Downloads\\GrafikUczelniPrzyklad.accdb')

cursor = connect.cursor()
query = "select * from pracownicy"
cursor.execute(query)
records = cursor.fetchall()

for i in range(len(records)):
    print(records[i])