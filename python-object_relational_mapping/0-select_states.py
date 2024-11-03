#!/usr/bin/python3
"""Module for Selecting states"""


from sys import argv
import MySQLdb

db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
cur = db.cursor()

cur.execute("SELECT * FROM states")

for state in cur.fetchall():
        print(state)
