import cgi
class GenericApi:
	def __init__(self, dao, postForm=''):
		self.dao = dao
		self.postForm = postForm

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

	def create_GET(self, server):
		server.send_response(200)
		server.send_header('Content-type', 'text/html')
		server.end_headers()
		output =""
		output += "<html><body>"
		output += self.postForm
		output += "</body></html>"
		server.wfile.write(output)
	
	def create_POST(self, server):
		server.send_response(301)
		server.send_header('Content-type', 'text/html')
		server.end_headers()
		ctype, pdict = cgi.parse_header(server.headers.getheader('content-type'))
		if ctype == 'multipart/form-data':
			fields = cgi.parse_multipart(server.rfile, pdict)
			item = fields.get('name')
			print item
			self.dao.add(item[0])
		output = ""
		output += "<html><body>"
		output += self.postForm
		output += "</body></html>"
		server.wfile.write(output)