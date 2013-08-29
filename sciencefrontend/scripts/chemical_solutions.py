from django.shortcuts import render
from sciencefrontend.models import Script
from django.http import HttpResponse
from periodictable import *

def chemical_solutions(request):
	"""
	Renders main view.

	RETURNS:

		a Django render() HttpResponse object
	"""
	
	try:
		s = Script.objects.get(name="xafs_sample_prep")
	except:
		des = "computes how to create a solution from a solid chemical."
		ttl = "Chemical Solution Preparation"
		s = Script(name="chemical_solutions", ttl=ttl, des=des)
		s.save()

	data = s.get_data()

	return render(request, data['template'], data)