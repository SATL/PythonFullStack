import cgi
from dao.restaurantDAO import RestaurantDAO
from genericDAOApi import GenericDAOApi

class RestaurantApi(GenericDAOApi):
	def __init__(self):
		restaurantDAO = RestaurantDAO() 
		GenericDAOApi.__init__(self, restaurantDAO)	