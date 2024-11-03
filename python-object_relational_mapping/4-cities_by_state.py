#!/usr/bin/python3
"""Module for Selecting cities"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name \
                    FROM cities c \
                    INNER JOIN states s ON s.id = c.state_id ")
    for city in cur.fetchall():
        print(city)
    cur.close()
    db.close()
