#!/usr/bin/python3

"""A script that lists all cities from a database assumong that there's
a foreign key relationship between the cities and states table
"""

import MySQLdb
import sys


def cities_by_state():
    """Implementation
    """
    user_name = sys.argv[1]
    ps_w = sys.argv[2]
    d_b = sys.argv[3]

    con = MySQLdb.connect(host="localhost", port=3306, user=user_name,
                        passwd=ps_w, db=d_b, charset="utf8")
    cursor = con.cursor()
    queries = """
    SELECT cities.id, cities.name
    FROM cities
    ORDER BY cities.id ASC;
    """

    cursor.execute(queries)
    results = cursor.fetchall()

    for items in results:
        print(items)

    cursor.close()
    con.close()


if __name__ == '__main__':
    cities_by_state()
