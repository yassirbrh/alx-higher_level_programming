#!/usr/bin/python3
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
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(nm)
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
