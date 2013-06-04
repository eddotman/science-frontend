from script_base import ScriptBase
from django.shortcuts import render

from numpy import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from django.http import HttpResponse


def data_plot(request):
	"""
	Renders main view.

	RETURNS:

		a Django render() HttpResponse object
	"""

	s = ScriptBase("data_plot")

	return render(request, s.template, {'script_name': s.script_name,  'js_link': s.js_link, 'script_link': s.script_link})


def data_plot_image(request, type):
	"""
	Renders a PNG/PDF/SVG plot of data from a textarea input.

	ARGUMENTS:

		(POSTdata) data: multiline input from a textarea field; should be two columns of x-y data with
		the first line as the axis labels.

		type: if the returned image should be PNG, PDF or SVG.

	RETURNS:

		an HttpResponse of the graph with the appropriate content type.
	"""
	
	fig = Figure(facecolor=(1,1,1))
	ax = fig.add_subplot(111)


	if request.method == "POST":
		return HttpResponse(request.POST["data"])
		#textdata = loadtxt(request.POST["data"], dtype='S')
		xlabel = textdata[0,0]
		ylabel = textdata[0,1]

		x = float(textdata[1:,0])
		y = float(textdata[1:,1])
	
	else:
		return None

	ax.plot(x, y, color='k', ls='-', lw='2.5')
	ax.set_xlabel(xlabel)
	ax.set_ylabel(ylabel)

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