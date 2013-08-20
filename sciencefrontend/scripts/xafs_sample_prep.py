from django.shortcuts import render
from sciencefrontend.models import Script
from django.http import HttpResponse
from mucal import *
from periodictable import *

def xafs_sample_prep(request):
	"""
	Renders main view.

	RETURNS:

		a Django render() HttpResponse object
	"""
	
	try:
		s = Script.objects.get(name="xafs_sample_prep")
	except:
		des = "computes absorption lengths and other data for XAFS samples."
		ttl = "XAFS Sample Prep Calculator"
		s = Script(name="xafs_sample_prep", ttl=ttl, des=des)
		s.save()

	data = s.get_data()

	return render(request, data['template'], data)

def xafs_sample_prep_get_abslen(request):
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

		res += "<tr><td>Molecular Mass:</td><td>" + str(round(mass,2)) + " g/mol </td></tr>"

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

		res += "<tr><td>Linear Absorption Coefficient:</td><td>" + str(round(mu,2)) + " 1/cm </td></tr>"

		#Compute absorption length
		abs_length= round((1/mu) * 10000, 2) #microns
		res += "<tr><td>Total X-ray Absorption Length:</td><td>" + str(round(abs_length,2)) + " microns </td></tr>"

		#Compute approx. total mass assuming 0.65 cm radius for pellet (standard size for Pike brand pellet press)
		total_mass = round(dens * (0.65**2) * 3.14159 * (abs_length/10000) * 1000, 2)

		res += "<tr><td>Pellet Mass (13mm diameter):</td><td>" + str(total_mass) + " mg</td></tr>"

		res += "</table>"

		return HttpResponse(res)
	else:
		return HttpResponse("POSTdata must be used!")
