import sqlite3
import sys
from datetime import datetime, timedelta
import Adafruit_DHT
from flask import Flask

#app = Flask(__name__)
#@app.route("/")
#def getInfo():
#    return "yo"




def log_values(sensor_id, temp, hum):
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	conn = sqlite3.connect('/home/pi/Adafruit_Python_DHT/examples/temp&humdLog.db')
	curs = conn.cursor()

        #curs.execute("drop table if exists climate");
	#curs.execute('''CREATE TABLE climate(rDatetime datetime, tempC integer, hum integer)''');

	curs.execute("INSERT INTO climate VALUES(?, ?, ?);",(dt, "{0:.2f}".format(temp), "{0:.2f}".format(hum)))

	conn.commit()
	conn.close()
	print("%s   Temperature in C = %s  Relative Humidity: %s " % (dt, "{0:.2f}".format(temp), "{0:.2f}".format(hum)))
	#print("Temperature in C = " + str(temp) + " Relative Humidity: " + str(hum))

pin = 4
sensor = Adafruit_DHT.DHT22
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
	log_values("1", temperature, humidity)
else:
	log_values("1", -999, -999)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

connection = sqlite3.connect("temp&humdLog.db")
connection.row_factory = dict_factory

cursor = connection.cursor()

cursor.execute("select * from climate")

# fetch all or one we'll go for all.

results = cursor.fetchall()

#print results

connection.close()

#if __name__ == '__main__':
#    app.run(debug= True, host= '0.0.0.0')
