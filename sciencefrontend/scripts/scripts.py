from django.shortcuts import render
from sciencefrontend.models import Script

def scripts(request):
	
	try:
		s = Script.objects.get(name="scripts")
	except:
		des = "_"
		ttl = "_"
		s = Script(name="scripts", ttl=ttl, des=des)
		s.save()

	data = s.get_data()

	#select all scripts (except home pages)
	scripts = Script.objects.exclude(name="home_content").exclude(name="about").exclude(name="scripts").exclude(name="contact").order_by("ttl")
	data["scripts"] = scripts

	return render(request, data["template"], data)