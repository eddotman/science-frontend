from django.shortcuts import render
from sciencefrontend.models import Script

def scripts(request):
	
	try:
		s = Script.objects.get(name='scripts')
	except:
		des = ""
		ttl = ""
		s = Script(name="scripts", ttl=ttl, des=des)
		s.save()

	data = s.get_data()

	return render(request, data['template'], data)