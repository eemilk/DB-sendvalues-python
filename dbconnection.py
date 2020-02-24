print("This is begin")
import os
import time
import mysql.connector
from datetime import datetime

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

temp_sensor = '../../../.././sys/bus/w1/devices/22-000000574643/w1_slave'
print("This is setup")

def temp_raw():
    f = open(temp_sensor, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = temp_raw()

    temp_output = lines[1].find('t=')
    if temp_output != -1:
        temp_string = lines[1].strip()[temp_output+2:]
        temp_c = float(temp_string) / 1000.0
        print("This is temp reader")
        return temp_c


sql = "INSERT INTO weather (temperature, time) VALUES (%s, %s)"
print("This is sql")

def main():
    print("This is main")
    try:
        mydb = mysql.connector.connect(
            host="iotkurssi3.c01qhrlhpdby.us-east-1.rds.amazonaws.com",
            user="admin",
            passwd="iotkurssi",
            database="iotkurssi",
        )
        mycursor = mydb.cursor()
        print("This is database connect")
            
    except mysql.connector.Error as err:
        print("something went wrong: {}".format(err))

    while True:
        
        print("This is loop")
        dtime = datetime.now()       
        val = (read_temp(), dtime)
        mycursor.execute(sql, val)
        mydb.commit()
        time.sleep(10)

        
main()





        
