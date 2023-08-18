#!/usr/bin/python3
"""A script that list all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


def list_states():
    """Establish a connection, execute an sql query, fetch and print results
    """
    stdin_args = sys.argv[1:]
    user_name = stdin_args[0]
    ps_word = stdin_args[1]
    d_b = stdin_args[2]

    connection = MySQLdb.connect(host="localhost", port=3306, user=user_name,
                                 passwd=ps_word, db=d_b, charset="utf8")

    cursor = connection.cursor()
    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    connection.close()


if __name__ == '__main__':
    list_states()
