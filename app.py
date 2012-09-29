#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings' 
from google.appengine.dist import use_library
use_library('django', '1.2')

from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

from data_model import #attribute, attribute_category

# attribute_query = attribute.all()
# attribute_category_query = attribute_query.attribute_category.title

class index(webapp.RequestHandler):
	def get(self):
		#attributes = attribute.all()
		template_values = {
		#	'attributes': attributes
		}
		path = os.path.join(os.path.dirname(__file__), 'templates/generate_idea.html')
		self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication([
	('/', index)
	],	debug=True)

def main():
	run_wsgi_app(application)

if __name__ == '__main__':
	main()