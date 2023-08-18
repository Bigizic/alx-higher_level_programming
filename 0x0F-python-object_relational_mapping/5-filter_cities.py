#!/usr/bin/python3

"""A script that takes in the name of a state as an argument and lists all
cities of that state
"""

import MySQLdb
import sys


def filter_cities():
    """Implemntation
    """
    state_name = sys.argv[4]

    con = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3], charset="utf8")

    cursor = con.cursor()
    query = """
    SELECT cities.id, cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))
    results = cursor.fetchall()
    for names in results:
        print(names)

    cursor.close()
    con.close()


if __name__ == '__main__':
    filter_cities()
