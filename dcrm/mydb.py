import mysql.connector 

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'newpassword123'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE company")

print("All Done!") 