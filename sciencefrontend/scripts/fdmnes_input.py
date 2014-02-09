from django.shortcuts import render
from sciencefrontend.models import Script
from django.http import HttpResponse
from periodictable import *

def fdmnes_input(request):
	"""
	Renders main view.

	RETURNS:

		a Django render() HttpResponse object
	"""
	
	try:
		s = Script.objects.get(name="fdmnes_input")
	except:
		des = "Prepares an input file for FDMNES"
		ttl = "FDMNES Input File Creator"
		s = Script(name="fdmnes_input", ttl=ttl, des=des)
		s.save()

	data = s.get_data()

	return render(request, data['template'], data)
