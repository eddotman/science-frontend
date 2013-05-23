from django.shortcuts import render
from numpy import *

def home(request):
	import datetime

	script_input = datetime.datetime.now()
	script_output = cos(pi)
	
	return render(request, 'home.html', {'script_input':script_input, 'script_output': script_output})

def function_plot_png(request, funct, arg, xmin, xmax, ymin, ymax, xlabel, ylabel):
	import matplotlib.pyplot as plt
	from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
	from matplotlib.figure import Figure
	from django.http import HttpResponse

	fig = Figure(facecolor=(1,1,1))
	ax = fig.add_subplot(111)

	x = eval(arg)

	function = eval(funct)

	ax.plot(x, function, color='k', ls='-', lw='2.0')
	ax.set_xlim(float(xmin), float(xmax))
	ax.set_ylim(float(ymin), float(ymax))
	ax.set_xlabel(xlabel)
	ax.set_ylabel(ylabel)

	canvas = FigureCanvas(fig)
	response = HttpResponse(content_type="image/png")

	canvas.print_png(response)
	
	return response