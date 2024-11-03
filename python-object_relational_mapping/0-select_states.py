#!/usr/bin/python3
"""Module for Selecting states"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    for state in cur.fetchall():
        print(state)
    cur.close()
    db.close()