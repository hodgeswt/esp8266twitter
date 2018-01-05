import cherrypy
from passlib.hash import pbkdf2_sha256
import requests

hash = pbkdf2_sha256.encrypt("VerySecretPassword")

class PostTweet(object):
	@cherrypy.expose
	def index(self):
		return "Hello world!"
	
	@cherrypy.expose
	def post_tweet(self, password="fail", maker_key="fail"):
		if pbkdf2_sha256.verify(password, hash):
			thestr = 'https://maker.ifttt.com/trigger/button_pressed/with/key/'
			with_key = thestr + maker_key
			r = requests.post(thestr+maker_key)
			return "<h1>Tweet Posted</h1><br /><h2>Will not work if reloaded immediately.</h2>"
		else:
			return "<h1>Go away, failure!</h1>"
		
if __name__ == '__main__':
	cherrypy.quickstart(PostTweet())