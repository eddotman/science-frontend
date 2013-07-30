from django.db import models

class Script (models.Model):
	"""
	Common object for all ScienceFrontend scripts.
	"""	

	name = models.CharField(max_length=100)
	des = models.CharField(max_length=300)
	ttl = models.CharField(max_length=100)

	def get_data(self):
		self.script_name = self.name + ".py"
		self.script_link = "https://github.com/eddotman/science-frontend/blob/master/sciencefrontend/scripts/" + self.name + ".py"
		self.js_link =  self.name + ".js"
		self.template = self.name + ".html"

		self.data = {
			'script_name': self.script_name,  
			'js_link': self.js_link, 
			'script_link': self.script_link, 
			'script_des':self.des,
			'script_title':self.ttl,
			'template': self.template
		}

		return self.data


class Datafile(models.Model):
	"""
	Uploaded user files
	"""
	datafile = models.FileField(upload_to='%Y/%m/%d')
