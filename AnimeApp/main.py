import os
import urllib
import json
import webapp2
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
	def get(self):
		
		url = "https://ghibliapi.herokuapp.com/films"
		data = urllib.urlopen(url).read()
		data = json.loads(data)
		ans = []
		for i in data:
			ans.append(i['title'])

		for i in range(len(ans)):
			self.response.write(ans[i]+"<br>")

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)

		