#!/usr/bin/python3
'''
    Script that takes in an argument and displays all values
    in the states table of hbtn_0e_0_usa where name matches the argument.
'''
import sys
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        charset="utf8")
    cur = conn.cursor()
    nm = sys.argv[4]
    query = "SELECT * FROM states WHERE name LIKE '{}'".format(nm)
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
