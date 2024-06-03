import mysql.connector

conn = mysql.connector.connect(host = 'localhost',
                               user = 'root',
                               password = '',
                               database = 'slownik')
mycursor = conn.cursor()

mycursor.execute("Select * from slowa")
myresult = mycursor.fetchall()
#gdy zapytanie modyfikuje bazę danych, używamy conn.commit() aby wysłać zmiany do serwera

print(myresult)

conn.close()