from genericDAO import GenericDAO
from mapper_setup import Restaurant

class RestaurantDAO(GenericDAO):
	def __init__(self):
		super(RestaurantDAO, self).__init__(Restaurant)

	def add(self, nameItem):
		obj = Restaurant(name=nameItem)
		super(RestaurantDAO, self).add(obj)