#!/usr/bin/python3

"""A script that adds the State or table Object "Louisiana" to a database
"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def model_state_insert():
    """A function that takes 3 arguments from stdin and connect to a MySQL
    server running on localhost on port 3306, proceeds to insert a word into
    database
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    obj = session.query(State).filter_by(name='Louisiana').first()
    print(obj.id)

    session.close()

if __name__ == '__main__':
    model_state_insert()
