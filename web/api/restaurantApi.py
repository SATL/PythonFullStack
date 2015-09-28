import cgi
from dao.restaurantDAO import RestaurantDAO
from GenericApi import GenericApi

class RestaurantApi(GenericApi):
	postForm = '''<form method='POST' enctype='multipart/form-data' action='/restaurants/new'><h2>What is the name of the restaurant?</h2><input name="name" type="text" ><input type="submit" value="Submit"> </form>'''
	def __init__(self):
		restaurantDAO = RestaurantDAO() 
		GenericApi.__init__(self, restaurantDAO, self.postForm)	