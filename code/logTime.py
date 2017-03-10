#!/usr/bin/python
# -*- coding: utf-8 -*-


#####https://docs.python.org/2/library/sqlite3.html###########


import sqlite3 as mydb
import sys
import time

con = None
list = None

try:
    con = mydb.connect('testTime.db')
    cur = con.cursor()

    def readTime():
        global list
        list = [time.strftime("%Y-%m-%d"),time.strftime("%H-%M-%S")]
        return list

    print readTime();

    def logTime():
        datetime = [time.strftime("%Y-%m-%d"), time.strftime("%H-%M-%S")]


        cur.execute("INSERT INTO datetime VALUES(?,?)", datetime)
        #cur.execute("INSERT INTO datetime3 VALUES(?)", date, time)
        con.commit()

    logTime()

except mydb.Error, e:

    print "Error %s:" % e.args[0]
    sys.exit(1)

finally:

    if con:
        con.close()
