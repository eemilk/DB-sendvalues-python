import mysql.connector
from datetime import datetime



sql = "INSERT INTO lampotila (temperature, datetime) VALUES (%s, %s)"

try:
        mydb = mysql.connector.connect(
            host="iotkurssi3.c01qhrlhpdby.us-east-1.rds.amazonaws.com",
            user="admin",
            passwd="iotkurssi",
            database="weather",
        )
        mycursor= mydb.cursor()
        
    except mysql.connector.Error as err:
        print("something went wrong: {}".format(err))


while True: 
        
        rcv = port.readline()
        
        dtime = datetime.now()       
        val = (rcv, dtime)
        mycursor.execute(sql, val)
        mydb.commit()
	time.sleep(1)