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
		s = Script.objects.get(name="chemical_solutions")
	except:
		des = "computes how to create a solution from a solid chemical."
		ttl = "Chemical Solution Preparation"
		s = Script(name="chemical_solutions", ttl=ttl, des=des)
		s.save()

	data = s.get_data()

	return render(request, data['template'], data)

def chemical_solutions_compute(request):
	"""
	Computes the mass of the compound needed.

	POSTDATA:

		chem: chemical compound
		conc: molar concentration
		vol: total volume in litres

	RETURNS:

		HttpResponse of the mass needed.
	"""

	if request.method == "POST":
		
		res = "<table class='table table-bordered'>"

		try:
			#Get POSTDATA
			chem = str(request.POST['chem'])
			conc = float(request.POST['conc'])
			vol = float(request.POST['vol'])
		except:
			res = "Input format error! Please fix and retry."
			return HttpResponse(res)


		#Parse formula
		form = formula(chem)
		res += "<tr><td>Compound:</td><td>" + chem + "</td></tr>"

		#Compute molecular mass
		mass = 0.0

		for elem in form.atoms:
			mass += form.atoms[elem]*elem.mass 

		res += "<tr><td>Molecular Mass:</td><td>" + str(round(mass,2)) + " g/mol </td></tr>"

		#Compute mass needed for solution
		mass_needed = mass * conc * vol


		res += "<tr><td>Mass Needed:</td><td>" + str(round(mass_needed,2)) + "</td></tr>"
		res += "<tr><td>Total Volume:</td><td>" + str(vol) + "</td></tr>"

		return HttpResponse(res)

