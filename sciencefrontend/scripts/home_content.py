from django.shortcuts import render
from sciencefrontend.models import Script

def home_content(request):
	
	try:
		s = Script.objects.get(name="home_content")
	except:
		des = "_"
		ttl = "_"
		s = Script(name="home_content", ttl=ttl, des=des)
		s.save()

	data = s.get_data()

	return render(request, data['template'], data)