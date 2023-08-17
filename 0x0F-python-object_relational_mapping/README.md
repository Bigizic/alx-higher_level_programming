## Install MySQLdb module version 2.0.x

    $ sudo apt-get install python3-dev
    $ sudo apt-get install libmysqlclient-dev
    $ sudo apt-get install zlib1g-dev
    $ sudo pip3 install mysqlclient
    ...
    $ python3
    >>> import MySQLdb
    >>> MySQLdb.version_info 
    (2, 0, 3, 'final', 0)


## Install SQLAlchemy module version 1.4.x

    $ sudo pip3 install SQLAlchemy
    ...
    $ python3
    >>> import sqlalchemy
    >>> sqlalchemy.__version__ 
    '1.4.22'

## 0-select_states.py:

Write a script that lists all states from the database
hbtn_0e_0_usa:

Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)

You must use the module MySQLdb (import MySQLdb)

Your script should connect to a MySQL server running on localhost at port 3306

Results must be sorted in ascending order by states.id

Results must be displayed as they are in the example below

Your code should not be executed when imported


## 1-filter_states.py:

Write a script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa:

Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)

You must use the module MySQLdb (import MySQLdb)

Your script should connect to a MySQL server running on localhost at port 3306

Results must be sorted in ascending order by states.id

Results must be displayed as they are in the example below

Your code should not be executed when imported


## 2-my_filter_states.py:




