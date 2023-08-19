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

Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.

Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (no argument validation needed)

## 3-my_safe_filter_states.py:

write a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!

Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (safe from MySQL injection)

You must use the module MySQLdb (import MySQLdb)

## 4-cities_by_state.py:

Write a script that lists all cities from the database hbtn_0e_4_usa

Your script should take 3 arguments: mysql username, mysql password and database name

You must use the module MySQLdb (import MySQLdb)

Your script should connect to a MySQL server running on localhost at port 3306

Results must be sorted in ascending order by cities.id

You can use only execute() once

## 5-filter_cities.py:

Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa

Your script should take 4 arguments: mysql username, mysql password, database name and state name (SQL injection free!)

## model_state.py, 6-model_state.py:

Write a python file that contains the class definition of a State and an instance Base = declarative_base():

State class:

	inherits from Base Tips

	links to the MySQL table states

	class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key

	class attribute name that represents a column of a string with maximum 128 characters and can’t be null


You must use the module SQLAlchemy

Your script should connect to a MySQL server running on localhost at port 3306

WARNING: all classes who inherit from Base must be imported before calling Base.metadata.create_all(engine)


## 7-model_state_fetch_all.py:

Write a script that lists all State objects from the database hbtn_0e_6_usa

Your script should take 3 arguments: mysql username, mysql password and database name

## 8-model_state_fetch_first.py:

Write a script that prints the first State object from the database hbtn_0e_6_usa

Your script should take 3 arguments: mysql username, mysql password and database name

You must use the module SQLAlchemy

You must import State and Base from model_state - from model_state import Base, State

if the table states is empty, print Nothing followed by a new line


## 9-model_state_filter_a.py:

Write a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa

## 10-model_state_my_get.py:

Write a script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa

## 11-model_state_insert.py:

Write a script that adds the State object “Louisiana” to the database hbtn_0e_6_usa

## 12-model_state_update_id_2.py:

Write a script that changes the name of a State object from the database hbtn_0e_6_usa

## 13-model_state_delete_a.py:

Write a script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa

## model_city.py, 14-model_city_fetch_by_state.py:

Write a Python file similar to model_state.py named model_city.py that contains the class definition of a City.

City class:

	inherits from Base (imported from model_state)
	links to the MySQL table cities
	class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
	class attribute name that represents a column of a string of 128 characters and can’t be null
	class attribute state_id that represents a column of an integer, can’t be null and is a foreign key to states.id

write a script 14-model_city_fetch_by_state.py that prints all City objects from the database hbtn_0e_14_usa:

Your script should take 3 arguments: mysql username, mysql password and database name

You must use the module SQLAlchemy

You must import State and Base from model_state - from model_state import Base, State

Results must be sorted in ascending order by cities.id

Results must be display as they are in the example below (<state name>: (<city id>) <city name>)


## ADVANCED TASKS

