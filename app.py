import cherrypy
import bcrypt
import requests
import os

hash = "$2b$12$6uw0MOUnw3RrmG4vxaba7.NKe9JQSZTQk4NuRNkg7UgYJLvqOhD4C"

class PostTweet(object):
	@cherrypy.expose
	def index(self):
		return '''
		<!DOCTYPE html>
		<html>
		<head></head>
		<body>
			<h1>Post Tweet</h1>
			<p>Triggers a Maker Event that posts a tweet on @willsesp8266</p>
			<br />
			<form method="get" action="post_tweet">
				<input type="password" value="password" name="password" />
				<input type="password" value="maker key" name="maker_key" />
				<button type="submit">Post</button>
			</form>
		</body>
		</html>
		'''
	
	@cherrypy.expose
	def post_tweet(self, password="fail", maker_key="fail"):
		if bcrypt.checkpw(password.encode('utf8'), hash.encode('utf8')):
			thestr = 'https://maker.ifttt.com/trigger/button_pressed/with/key/'
			with_key = thestr + maker_key
			r = requests.post(thestr+maker_key)
			return "<!DOCTYPE html><html><head></head><body><h1>Tweet Posted</h1><br /><h2>Will not work if reloaded immediately.</h2></body></html>"
		else:
			return "<!DOCTYPE html><html><head></head><body><h1>Go away, failure!</h1></body></html>"
		
cherrypy.config.update({'server.socket_host': '0.0.0.0',})
cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '5000')),})
cherrypy.quickstart(PostTweet())
	
	