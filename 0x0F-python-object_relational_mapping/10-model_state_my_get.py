#!/usr/bin/python3

"""A script that prints the State object with the name passed as argument
"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def model_state_my_get():
    """A function that takes 4 arguments from stdin, connects to MySQL server
    running on localhost at port 3306 and prints the state object with the name
    to search passed as 4th argument
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    fetch_states = session.query(State).filter(
                    State.name.like('%{}%').format(sys.argv[4])
                    ).order_by(State.id)

    if (fetch_states):
        for states in fetch_states:
            print(states.id)
    else:
        print("Not found")

    session.close()


if __name__ == '__main__':
    model_state_my_get()
