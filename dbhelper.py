from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session  # orm(object relational mapping) - every class definition, each class gets converted into a table
from sqlalchemy.ext.declarative import declarative_base
#Engin a class connects Pool and dialect together to provide a source
#of database connectivity and behaviour 
#An obj of Engine class is instantiated using create_engine funct
#create_engine funct takes the database as one argument.
engine = create_engine('sqlite:///test.db', echo=False)#echo flag is shortcut to set up sqlalchemy
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
Base = declarative_base()
