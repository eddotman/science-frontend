from script_base import ScriptBase
from django.shortcuts import render

from numpy import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from django.http import HttpResponse
from base64 import *


def function_plot(request):

	s = ScriptBase("function_plot")

	return render(request, s.template, {'script_name': s.script_name,  'js_link': s.js_link, 'script_link': s.script_link})


def function_plot_image(request, funct, xmin, xmax, xincrem, type):

	fig = Figure(facecolor=(1,1,1))
	ax = fig.add_subplot(111)

	x = arange(float(xmin), float(xmax), float(xincrem))
	y = eval(funct)

	ax.plot(x, y, color='k', ls='-', lw='2.5')
	ax.set_xlabel('X')
	ax.set_ylabel('Y')

	canvas = FigureCanvas(fig)

	if type == "png":
		response = HttpResponse(content_type="image/png")
		canvas.print_png(response)
	elif type == "pdf":
		response = HttpResponse(content_type="application/pdf")
		canvas.print_pdf(response)
	elif type == "svg":
		response = HttpResponse(content_type="image/x-svg")
		canvas.print_svg(response)
	else:
		response = None
	
	return response