#!/usr/bin/python3

"""A script that lists all states with a name starting with N
"""

import MySQLdb
import sys


def list_states_n():
    """Establish a connection, execute an sql query, fetch and print result
    of states starting with a captial N
    """
    stdin_args = sys.argv[1:]
    user_name = stdin_args[0]
    ps_word = stdin_args[1]
    d_b = stdin_args[2]
    arg = stdin_args[3]

    connection = MySQLdb.connect(host="localhost", port=3306, user=user_name,
                                 passwd=ps_word, db=d_b, charset="utf8")
    cursor = connection.cursor()
    query = "SELECT * FROM states WHERE name = {} ORDER BY id ASC".format(arg)
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    connection.close()


if __name__ == '__main__':
    list_states_n()
