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
    cursor.execute("""SELECT cities.name
                   FROM cities
                   INNER JOIN states ON states.id=cities.state_id
                   WHERE states.name=%s""", (state_name,))
    results = cursor.fetchall()
    tmp = [names[0] for names in results]
    output = ', '.join(tmp)
    print(output)

    cursor.close()
    con.close()


if __name__ == '__main__':
    filter_cities()
