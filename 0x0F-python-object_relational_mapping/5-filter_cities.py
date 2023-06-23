#!/usr/bin/python3
"""
listscities 
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT * FROM cities
                INNER JOIN states
                state_id = states.id
                ORDER BY cities.id""")
    print(", ".join([city[2]
                     for city in c.fetchall()
                     if city[4] == sys.argv[4]]))
