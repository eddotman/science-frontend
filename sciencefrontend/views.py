from django.shortcuts import render
import datetime

def test_output(request):
	now = datetime.datetime.now()
	return render(request, 'home.html', {'test_output':now})