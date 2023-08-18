#!/usr/bin/python3

"""A script that lists all states with a name starting with N
"""

import MySQLdb
import sys


def list_states_n():
    """Establish a connection, execute an sql query, fetch and print result
    of states starting with a captial N
    """
    user_name = sys.argv[1]
    ps_word = sys.argv[2]
    d_b = sys.argv[3]
    arg = sys.argv[4]

    connection = MySQLdb.connect(host="localhost", port=3306, user=user_name,
                                 passwd=ps_word, db=d_b, charset="utf8")
    cursor = connection.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}'ORDER BY id ASC"\
            .format(arg)
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    connection.close()


if __name__ == '__main__':
    list_states_n()
