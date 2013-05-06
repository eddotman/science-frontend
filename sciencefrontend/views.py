from django.shortcuts import render
from numpy import *
import datetime

def test_output(request):
	now = datetime.datetime.now()
	test_numpy = cos(pi)
	return render(request, 'home.html', {'test_output':now, 'numpy_output': test_numpy})