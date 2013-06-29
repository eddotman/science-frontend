from django.shortcuts import render


def home(request):
	from scripts.home_content import echo_home

	script_name = "home_content.py"
	script_link = "https://github.com/eddotman/science-frontend/blob/master/sciencefrontend/scripts/home_content.py"
	script_gui = echo_home()
	
	return render(request, 'home.html', {'script_name': script_name, 'script_link': script_link, 'script_gui': script_gui})
