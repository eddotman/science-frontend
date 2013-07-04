from script_base import ScriptBase
from django.shortcuts import render
from django.http import HttpResponse
from mucal import *
from periodictable import *

def xafs_sample_prep(request):
	"""
	Renders main view.

	RETURNS:

		a Django render() HttpResponse object
	"""

	des = "computes absorption lengths and other data for XAFS samples."
	s = ScriptBase("xafs_sample_prep", des)

	return render(request, s.template, {'script_name': s.script_name,  'js_link': s.js_link, 'script_link': s.script_link, 'script_des':s.script_des})

def get_abslen(request):
	"""
	Computes the relevant x-ray absorption data.

	POSTDATA:
	
		chem: Element chemical formula.
		ephot: Photon energy (incoming) in keV.
		dens: Compound density in g/cc

	RETURNS:

		Total xray absorption length.
	"""

	if request.method == "POST":
		
		#Get POSTDATA
		chem = str(request.POST['chem'])
		ephot = float(request.POST['ephot'])
		dens = float(request.POST['dens'])

		#Parse formula
		form = formula(chem)

		#Compute molecular mass
		mass = 0.0

		for elem in form.atoms:
			mass += form.atoms[elem]*elem.mass

		#Compute total mu
		mu = 0.0
		for elem in form.atoms:
			frac = (form.atoms[elem]*elem.mass) / mass
			mu += frac * get_total_xsec(elem.symbol, ephot)
		mu *= dens

		abs_length= round((1/mu) * 10000, 2) #microns

		return HttpResponse(abs_length)
	else:
		return HttpResponse("POSTdata must be used!")
