import cgi
class GenericDAOApi:
	def __init__(self, dao):
		self.dao = dao

	def getAll(self, server):
		server.send_response(200)
		server.send_header('Content-type', 'text/html')
		server.end_headers()
		output = ""
		output += "<html><body>"
		output += "<p>"
		all = self.dao.findAll()
		for obj in all:
			output+=obj.name+'<br>'
			output+="<a href='restaurant/"+str(obj.id)+"'>Edit</a>    "
			output+="<a href='restaurant/"+str(obj.id)+"'>Remove</a>"
			output +='</p><hr>'
		output += "</body></html>"
		server.wfile.write(output)
		return

	def getOne(self, server, id):
		server.send_response(200)
		server.send_header('Content-type', 'text/html')
		server.end_headers()
		output = ""
		output += "<html><body>"
		output += "<ul>"
		obj = self.dao.get(id)
		output+='<li>'+obj.name+'</li>'
		output +='</ul>'
		output += "</body></html>"
		server.wfile.write(output)
		return