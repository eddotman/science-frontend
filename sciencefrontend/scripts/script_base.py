
class ScriptBase:
	"""
	Common behaviour shared by all ScienceFrontend scripts.
	"""	

	def __init__(self, name, title=None, des=None):
		self.name = name
		self.script_name = self.name + ".py"

		if title is None: 
			self.title = self.name
		else:
			self.title = title

		self.script_des = des
		self.script_link = "https://github.com/eddotman/science-frontend/blob/master/sciencefrontend/scripts/" + self.name + ".py"
		self.js_link =  name + ".js"
		self.template = name + ".html"

		self.data = {
			'script_name': self.script_name,  
			'js_link': self.js_link, 
			'script_link': self.script_link, 
			'script_des':self.script_des,
			'script_title':self.title
		}

	def db_init(self):
		return None