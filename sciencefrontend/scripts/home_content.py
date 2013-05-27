from django.shortcuts import render
from script_base import ScriptBase

def home_content(request):
	
	script = ScriptBase("home_content")

	return render(request, 'home.html', {'script_name': script.script_name, 'script_link': script.script_link, 'script_gui': script.script_gui})
