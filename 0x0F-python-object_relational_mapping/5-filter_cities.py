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
        """SELECT cities.name FROM cities
        JOIN states ON states.id = cities.state_id
        WHERE states.name LIKE %s ORDER BY cities.id ASC""", (sys.argv[4], ))
    query_rows = cur.fetchall()
    for row in query_rows:
        if row != query_rows[len(query_rows) - 1]:
            print(row[0], end=", ")
        else:
            print(row[0])
    cur.close()
    conn.close()
