#!/usr/bin/python3
'''
    Script that lists all cities from the database hbtn_0e_4_usa.
'''
import sys
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        port=3306,
        charset="utf8"
        )
    cur = conn.cursor()
    cur.execute(
        """SELECT cities.id, cities.name, states.name FROM cities
        JOIN states ON states.id = cities.state_id ORDER BY cities.id ASC;""")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
