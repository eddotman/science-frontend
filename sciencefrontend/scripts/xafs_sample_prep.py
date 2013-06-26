from script_base import ScriptBase
from django.shortcuts import render
from django.http import HttpResponse
from mucal import *

from numpy import *


def xafs_sample_prep(request):
	"""
	Renders main view.

	RETURNS:

		a Django render() HttpResponse object
	"""

	des = "computes absorption lengths and other data for XAFS samples."
	s = ScriptBase("xafs_sample_prep", des)

	return render(request, s.template, {'script_name': s.script_name,  'js_link': s.js_link, 'script_link': s.script_link, 'script_des':s.script_des})

def get_xcross(request):
	"""
	Computes the relevant x-ray absorption data.

	RETURNS:

		Total xray absorption cross section.
	"""
	
	elemName = "As"
	energy = 11.9
	print_flag = 0
	retEnergy = zeros(9)
	xsec = zeros(11)
	fl_yield = zeros(4)
 	err_msg = empty(100)
 	elemName = empty(2)

	mucal(elemName, 0, energy, 'c', print_flag, retEnergy, xsec, fl_yield, err_msg)

	return HttpResponse(xsec[3])