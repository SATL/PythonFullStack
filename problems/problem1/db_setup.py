import sys

from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Shelter(Base):
	__tablename__ = 'shelter'

	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable=False)
	adress = Column(String(80))
	city = Column(String(80))
	state = Column(String(80))
	email = Column(String(80))


class Puppy(Base):
	__tablename__ = 'puppy'

	id = Column(Integer, primary_key=True)
	name = Column(String(80), nullable = False)
	date_of_birth = Column(Date)
	breed = Column(String(80))
	gender = Column(String(80))
	weight = Column(String(80))

	shelter_id = (Integer, ForeignKey('shelter.id'))
	shelter = relationship(Shelter)

engine = create_engine('sqlite:///problem1.db')
Base.metadata.create_all(engine)
