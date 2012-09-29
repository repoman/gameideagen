#!/usr/bin/env python
# -*- coding: utf-8 -*-

from google.appengine.ext import db

class crew_member(db.Model):
	pseudonym = db.StringProperty()
	username = db.StringProperty()
	profile_views = db.IntegerProperty(default=0)
	last_modified = db.DateTimeProperty(auto_now=True)
	created = db.DateTimeProperty(auto_now_add=True)

#class attribute(db.Model):
#	title = db.StringProperty()
#	category_key = db.ReferenceProperty(attribute_category)
#	created = db.DateTimeProperty(auto_now_add=True)
#	last_modified = db.DateTimeProperty(auto_now=True)
#
#class attribute_category(db.Model):
#	title = db.StringProperty()
#	created = db.DateTimeProperty(auto_now_add=True)
#	last_modified = db.DateTimeProperty(auto_now=True)#