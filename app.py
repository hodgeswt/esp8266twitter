import cherrypy
import bcrypt
import requests
import os

hash = "$2b$12$6uw0MOUnw3RrmG4vxaba7.NKe9JQSZTQk4NuRNkg7UgYJLvqOhD4C"

class PostTweet(object):
	@cherrypy.expose
	def index(self):
		return "Hello world!"
	
	@cherrypy.expose
	def post_tweet(self, password="fail", maker_key="fail"):
		if bcrypt.checkpw(password.encode('utf8'), hash):
			thestr = 'https://maker.ifttt.com/trigger/button_pressed/with/key/'
			with_key = thestr + maker_key
			r = requests.post(thestr+maker_key)
			return "<h1>Tweet Posted</h1><br /><h2>Will not work if reloaded immediately.</h2>"
		else:
			return "<h1>Go away, failure!</h1>"
		
cherrypy.config.update({'server.socket_host': '0.0.0.0',})
cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '5000')),})
cherrypy.quickstart(PostTweet())
	
	