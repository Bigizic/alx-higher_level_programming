#!/usr/bin/python3
"""A script that acts like 2-my_ilter_states but it's safe from an SQL
injection
"""

import MySQLdb
import sys


def my_safe_filter_states():
    """Establish a connection, execute an sql query, fetch and print result
    of states that match 4th argument but it's safe from an SQL injection
    """
    user_name = sys.argv[1]
    ps_word = sys.argv[2]
    d_b = sys.argv[3]
    arg = sys.argv[4]

    con = MySQLdb.connect(host="localhost", port=3306, user=user_name,
                          passwd=ps_word, db=d_b, charset="utf8")
    cursor = con.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    cursor.execute(query, ('%' + arg + '%',))
    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    con.close()


if __name__ == '__main__':
    my_safe_filter_states()
