from script_base import ScriptBase
from django.shortcuts import render
from django.http import HttpResponse
from mucal import *

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

	ARGUMENTS:
	
		elem: Element chemical symbol.
		ephot: Photon energy (incoming) in keV.

	RETURNS:

		Total xray absorption length.
	"""

	if request.method == "POST":
		elem = str(request.POST['elem'])
		ephot = float(request.POST['ephot'])
		dens = float(request.POST['dens'])
		abs_length= round(1/(dens*get_total_xsec(elem, ephot))*10000, 2) #microns

		return HttpResponse(abs_length)
	else:
		return HttpResponse("POSTdata must be used!")
