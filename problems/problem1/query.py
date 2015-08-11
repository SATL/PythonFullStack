from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import time
from datetime import date, timedelta, datetime
from puppies import Puppy, Shelter, Base

def printPuppies(puppies, attr='dateOfBirth'):
	# print attr
	for puppy in puppies:
		print puppy.name
		print getattr(puppy,attr)

engine = create_engine('sqlite:///puppyshelter.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession();

#printing by name
puppies = session.query(Puppy).order_by("name")
printPuppies(puppies)

#printing by date og birth
current_time = datetime.utcnow()
six_months_ago = current_time - timedelta(days=30*6)
puppies = session.query(Puppy).filter(Puppy.dateOfBirth < six_months_ago ).order_by("dateOfBirth desc")
printPuppies(puppies)


#printint by weight
puppies = session.query(Puppy).order_by("weight")
printPuppies(puppies, 'weight')

#printint by shelter
puppies = session.query(Puppy).group_by(Puppy.shelter_id).all()
printPuppies(puppies, 'shelter_id')