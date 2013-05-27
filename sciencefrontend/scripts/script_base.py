import os

class ScriptBase:

	def __init__(self, name):
		self.name = name

		self.script_name = self.name + ".py"
		self.script_link = "https://github.com/eddotman/science-frontend/blob/master/sciencefrontend/scripts/" + self.name + ".py"

		html_content = open(os.path.dirname(__file__) + "\\html_content\\" + name + ".html")
		self.js_link =  name + ".js"
		self.script_gui = html_content.read()