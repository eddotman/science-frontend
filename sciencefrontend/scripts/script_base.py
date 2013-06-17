
class ScriptBase:
	"""
	Common behaviour shared by all ScienceFrontend scripts.
	"""	

	def __init__(self, name, des=None):
		self.name = name
		self.script_name = self.name + ".py"
		self.script_des = des
		self.script_link = "https://github.com/eddotman/science-frontend/blob/master/sciencefrontend/scripts/" + self.name + ".py"
		self.js_link =  name + ".js"
		self.template = name + ".html"