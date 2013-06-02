from django.shortcuts import render
from script_base import ScriptBase

def home_content(request):
	
	s = ScriptBase("home_content")

	return render(request, s.template, {'script_name': s.script_name, 'script_link': s.script_link})
