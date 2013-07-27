from sciencefrontend.models import Script
from django.shortcuts import render

from numpy import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from django.http import HttpResponse


def function_plot(request):
	"""
	Renders main view.

	RETURNS:

		a Django render() HttpResponse object
	"""

	try:
		s = Script.objects.get(name="function_plot")
	except:
		des = "plots a function as a high-quality graph (PNG + PDF + SVG)."
		ttl = "Mathematical Function Plotter"
		s = Script(name="function_plot", ttl=ttl, des=des)
		s.save()

	data = s.get_data()

	return render(request, data['template'], data)


def function_plot_image(request, funct, xmin, xmax, type):
	"""
	Creates an HttpResponse PNG/PDF/SVG plot of a given function_plot.

	ARGUMENTS:

		funct: the function to be plotted.
		xmin: minimum x value.
		xmax: maximum x value.
		type: the type of response to return.

	RETURNS:

		An HttpResponse of the appropriate type (PNG/PDF/SVG) containing the plot.

	"""

	fig = Figure(facecolor=(1,1,1))
	ax = fig.add_subplot(111)

	xincrem = (float(xmax) - float(xmin))/1000.0
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