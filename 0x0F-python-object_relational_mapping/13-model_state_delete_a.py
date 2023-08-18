#!/usr/bin/python3

"""A script that deletes all State objects with a name containing the letter
a from a database
"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def model_state_delete_a():
    """A function that takes 3 arguments from stdin, connects to a MySQL
    server running on localhost at port 3306 and procceds to delete all State
    objects with a name containing the letter a from a database
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    fetch_states = session.query(State).filter(State.name.like('%a%'))
    for states in fetch_states:
        session.delete(states)

    session.commit()

    session.close()


if __name__ == '__main__':
    model_state_delete_a()
