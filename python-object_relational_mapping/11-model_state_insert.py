#!/usr/bin/python3
"""Adds the State "Louisiana" to the database hbtn_0e_6_usa.

Prints the id of the newly created State after committing.

Usage: ./11-model_state_insert.py <mysql username> <mysql password>
                                  <database name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    louisiana = State(name="Louisiana")
    session.add(louisiana)
    session.commit()
    print(louisiana.id)
