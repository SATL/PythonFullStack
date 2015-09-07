
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from mapper_setup import Restaurant, Base, MenuItem

class GenericDAO:
	__database__ = 'sqlite:///restaurantmenu.db'
	def __init__(self, orm_object):		
		engine = create_engine(self.__database__)
		Base.metadata.bind = engine
		DBSession = sessionmaker(bind=engine)
		self.session = DBSession()
		self.orm_object = orm_object

	def findAll(self):
		return self.session.query(self.orm_object)

	def get(self, id):
		return self.session.query(self.orm_object).get(id)

	def add(self, obj):
		created = self.session.add(obj)
		self.session.commit()
		return created

	def update(self, obj):
		self.session.commit()
