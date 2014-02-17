from django.shortcuts import render
from sciencefrontend.models import Script

def about(request):
	
	try:
		s = Script.objects.get(name="about")
	except:
		des = "_"
		ttl = "_"
		s = Script(name="about", ttl=ttl, des=des)
		s.save()

	data = s.get_data()

	return render(request, data['template'], data)