from django.shortcuts import render
from script_base import ScriptBase

def about(request):
	
	s = ScriptBase("about")

	return render(request, s.template, {'script_name': s.script_name, 'script_link': s.script_link})