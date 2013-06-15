from script_base import ScriptBase
from django.shortcuts import render

from numpy import *


def xafs_sample_prep(request):
	"""
	Renders main view.

	RETURNS:

		a Django render() HttpResponse object
	"""

	s = ScriptBase("xafs_sample_prep")

	return render(request, s.template, {'script_name': s.script_name,  'js_link': s.js_link, 'script_link': s.script_link})