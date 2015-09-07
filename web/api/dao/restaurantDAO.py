from genericDAO import GenericDAO
from mapper_setup import Restaurant

class RestaurantDAO(GenericDAO):
	def __init__(self):
		GenericDAO.__init__(self, Restaurant)
