import cgi

class helloApi:

	def helloGet(self, server):
		server.send_response(200)
		server.send_header('Content-type', 'text/html')
		server.end_headers()
		output = ""
		output += "<html><body>"
		output += "<h1>Hello!</h1>"
		output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
		output += "</body></html>"
		server.wfile.write(output)
		# print output
		return

	def holaGet(self, server):
		server.send_response(200)
		server.send_header('Content-type', 'text/html')
		server.end_headers()
		output = ""
		output += "<html><body>"
		output += "<h1>&#161 Hola !</h1>"
		output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
		output += "</body></html>"
		server.wfile.write(output)
		# print output
		return

	def helloPost(self, server):
		server.send_response(301)
		server.send_header('Content-type', 'text/html')
		server.end_headers()
		ctype, pdict = cgi.parse_header(server.headers.getheader('content-type'))
		if ctype == 'multipart/form-data':
			fields = cgi.parse_multipart(server.rfile, pdict)
			messagecontent = fields.get('message')
		output = ""
		output += "<html><body>"
		output += " <h2> Okay, how about this: </h2>"
		output += "<h1> %s </h1>" % messagecontent[0]
		output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
		output += "</body></html>"
		server.wfile.write(output)
		# print output
			