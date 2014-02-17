from django.shortcuts import render
from sciencefrontend.models import Script

def contact(request):
	
	try:
		s = Script.objects.get(name="contact")
	except:
		des = "_"
		ttl = "_"
		s = Script(name="contact", ttl=ttl, des=des)
		s.save()

	data = s.get_data()

	return render(request, data['template'], data)