
class ScriptBase:

	def __init__(self, name):
		self.name = name
		self.script_name = self.name + ".py"
		self.script_link = "https://github.com/eddotman/science-frontend/blob/master/sciencefrontend/scripts/" + self.name + ".py"
		self.js_link =  name + ".js"
		self.template = name + ".html"