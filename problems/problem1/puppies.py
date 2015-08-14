from sqlalchemy import Table, Column, ForeignKey, Integer, String, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
 
Base = declarative_base()

association_table = Table('association', Base.metadata, Column('puppy_id', Integer, ForeignKey('puppy.id')), Column('adopters_id', Integer, ForeignKey('adopters.id')))

class Shelter(Base):
    __tablename__ = 'shelter'
    id = Column(Integer, primary_key = True)
    name =Column(String(80), nullable = False)
    address = Column(String(250))
    city = Column(String(80))
    state = Column(String(20))
    zipCode = Column(String(10))
    website = Column(String)
    
class Puppy(Base):
    __tablename__ = 'puppy'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(6), nullable = False)
    dateOfBirth = Column(Date)
    picture = Column(String)
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship(Shelter)
    weight = Column(Numeric(10))
    profile = relationship("PuppyProfile", uselist=False, backref="puppy")
    adopters = relationship("Adopters", secondary=association_table, backref="puppies")

class PuppyProfile(Base):
    __tablename__='puppy_profile'
    id = Column(Integer, primary_key=True)
    photo = Column(String(80))
    description = Column(String(250))
    needs = Column(String(100))
    puppy_id = Column(Integer, ForeignKey('puppy.id'))

class Adopters(Base):
    __tablename__='adopters'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    address = Column(String(100))
    phone = Column(String(80))



engine = create_engine('sqlite:///puppyshelter.db')
 

Base.metadata.create_all(engine)