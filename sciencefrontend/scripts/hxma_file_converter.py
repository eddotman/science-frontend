from sciencefrontend.models import Script
from django.shortcuts import render

def hxma_file_converter(request):
	"""
	Renders main view.

	RETURNS:

		a Django render() HttpResponse object
	"""

	try:
		s = Script.objects.get(name="hxma_file_converter")
	except:
		des = "converts a data file in HXMA (Canadian Light Source) format to a standard DAT file."
		ttl = "HXMA Data File Converter"
		s = Script(name="hxma_file_converter", ttl=ttl, des=des)
		s.save()

	data = s.get_data()

	return render(request, data['template'], data)