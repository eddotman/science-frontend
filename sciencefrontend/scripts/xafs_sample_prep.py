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
		bn: Boron Nitride dilution fraction (between 0-1)

	RETURNS:

		X-ray data as an HTTPresponse string.
	"""

	if request.method == "POST":
		
		res = "<table class='table table-bordered'>"

		try:
			#Get POSTDATA
			chem = str(request.POST['chem'])
			ephot = float(request.POST['ephot'])
			dens = float(request.POST['dens'])
			bn = float(request.POST['bn'])
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

		res += "<tr><td>Molecular Mass:</td><td>" + str(mass) + " g/mol </td></tr>"

		#Compute total mu
		mu = 0.0
		for elem in form.atoms:
			frac = (form.atoms[elem]*elem.mass) / mass
			mu += frac * get_total_xsec(elem.symbol, ephot)

		#Perform dilution with BN if needed
		if str(bn) != "" and 0 < bn < 1:
			bn_mass = B.mass + N.mass
			bn_dens = 2.29 #source: Sigma-Aldrich, BN powder ~1 micron, 98%
			frac_b = B.mass / bn_mass
			frac_n = N.mass / bn_mass

			dens = (1 - bn) * dens + bn * bn_dens

			mu_bn = (frac_b * get_total_xsec(B.symbol, ephot) + frac_n * get_total_xsec(N.symbol, ephot))
			mu = (1 - bn) * mu + bn * mu_bn

			res += "<tr><td>BN Dilution Fraction:</td><td>" + str(bn) + "</td></tr>"

		mu *= dens

		res += "<tr><td>Linear Absorption Coefficient:</td><td>" + str(mu) + " 1/cm </td></tr>"

		#Compute absorption length
		abs_length= round((1/mu) * 10000, 2) #microns
		res += "<tr><td>Total X-ray Absorption Length:</td><td>" + str(abs_length) + " microns </td></tr>"

		res += "</table>"

		return HttpResponse(res)
	else:
		return HttpResponse("POSTdata must be used!")
