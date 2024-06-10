import mysql.connector

conn = mysql.connector.connect(host = 'localhost',
                               user = 'root',
                               password = '',
                               database = 'slownik')
mycursor = conn.cursor()

#mycursor.execute("Select polski,angielski from slowa")
#myresult = mycursor.fetchall()
#gdy zapytanie modyfikuje bazę danych, używamy conn.commit() aby wysłać zmiany do serwera

#for x in myresult:
#    print(x[0] + " - " + x[1])
def Wyszukaj():
    slowo = input("Podaj słowo:")
    mycursor.execute("SELECT polski, angielski from slowa where polski = '" + slowo + "' OR angielski = '" + slowo + "'")
    myresult = mycursor.fetchall()
    if(len(myresult) == 0):
        print("Nie ma takiego słówka w słowniku")
    for x in myresult:
        print(x[0] + " - " + x[1])
def Dodaj():
    polskieSlowo = input("Podaj słówko po polsku:")
    angielskieSlowo = input("Podaj znaczenie tego słowa po angielsku:")
    mycursor.execute("SELECT polski, angielski from slowa where polski = '" + polskieSlowo + "' and angielski = '" +angielskieSlowo + "'")
    myresult = mycursor.fetchall()
    if(len(myresult) == 0):
        mycursor.execute("INSERT INTO `slowa`(`polski`, `angielski`) VALUES ('" + polskieSlowo + "','" + angielskieSlowo + "')")
        conn.commit()
        print("Słówko zostało dodane do bazy danych")
    else:
        print("Takie słówko oraz jego tłumaczenie znajduje się już w bazie danch")

def Usun():
    slowo = input("Podaj słówko po polsku lub po angielsku:")
    mycursor.execute("SELECT id, polski, angielski from slowa where polski = '" + slowo + "' or angielski = '" + slowo + "'")
    myresult = mycursor.fetchall()
    if(len(myresult) == 0):
        print("Nie ma takiego słówka")
    if(len(myresult) == 1):
        usun = input("Czy na pewno chcesz usunąć: " + myresult[0][1] + " - " + myresult[0][2]+"? Jeśli tak wpisz 1, jeśli nie 0: ")
        if(usun == "1"):
            mycursor.execute("DELETE FROM `slowa` WHERE id=" + str(myresult[0][0]))
            conn.commit()
            print("Słówko zostało usunięte")
        else:
            print("Słówko nie zostało usunięte")
    else:
        #for x in myresult:





while True:
    print("""
    1. Wyszukaj słówko w słowniku
    2. Dodaj słówko do słownika
    3. Usuń słówko w słowniku
    4. Wyświetl zawartość słownika
    5. Wyjście
    """)
    opcja = input("Wybierz opcję: ")
    print("==================================================================")
    match opcja:
        case "1":
            Wyszukaj()
        case "2":
            Dodaj()
        case "3":
            Usun()
        case "4":
            PokazSlownik()
        case "5":
            conn.close()
            exit()
        case other:
            print("Nie ma takiej opcji")
