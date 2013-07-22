from script_base import ScriptBase
from django.shortcuts import render

def hxma_file_converter(request):
	"""
	Renders main view.

	RETURNS:

		a Django render() HttpResponse object
	"""

	des = "converts a data file in HXMA (Canadian Light Source) format to a standard DAT file."
	ttl = "HXMA Data File Converter"
	s = ScriptBase("hxma_file_converter", title=ttl, des=des)

	return render(request, s.template, s.data)