from sciencefrontend.models import Script, Datafile
from django.shortcuts import render
from django.http import HttpResponse
from numpy import *
import json

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

def hxma_file_converter_upload(request):
    # Handle file upload
    if request.method == 'POST':
        form = request.FILES
    
        newdata = Datafile(datafile = form['file'])
        newdata.save()

        f = loadtxt(newdata.datafile.path, delimiter=",")
        savetxt(newdata.datafile.path, f)
        
        # Return link
        return HttpResponse(newdata.datafile.path)