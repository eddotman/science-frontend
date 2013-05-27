from django.shortcuts import render

def home_content(request):
	import os

	name = "home_content"

	script_name = name + ".py"
	script_link = "https://github.com/eddotman/science-frontend/blob/master/sciencefrontend/scripts/" + name + ".py"

	html_content = open(os.path.dirname(__file__) + "\\html_content\\" + name + ".html")
	script_gui = html_content.read()

	return render(request, 'home.html', {'script_name': script_name, 'script_link': script_link, 'script_gui': script_gui})
