from sciencefrontend.models import Script
from django.shortcuts import render

from numpy import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from django.http import HttpResponse
from shlex import split


def data_plot(request):
	"""
	Renders main view.

	RETURNS:

		a Django render() HttpResponse object
	"""

	try:
		s = Script.objects.get(name="data_plot")
	except:
		des = "plots two-column data as a high-quality graph (PNG + PDF + SVG)."
		ttl = "Two-Column Data Plotter"
		s = Script(name="data_plot", ttl=ttl, des=des)
		s.save()

	data = s.get_data()

	return render(request, data['template'], data)


def data_plot_image(request):
	"""
	Renders a PNG/PDF/SVG plot of data from a textarea input.

	ARGUMENTS:

		(POSTdata) data: multiline input from a textarea field; should be two columns of x-y data with
		the first line as the axis labels.

	RETURNS:

		an HttpResponse with a reference to the plot path.
	"""

	if request.method == "POST":
		
		textdata = str.splitlines(str(request.POST["data"]))
		splitdata = empty((0,2))

		for line in textdata:
			splitdata = vstack((splitdata, split(line)))

		xlabel = splitdata[0][0]
		ylabel = splitdata[0][1]

		x = empty((1,0))
		y = empty((1,0))

		x = transpose(splitdata[1:,0])
		y = transpose(splitdata[1:,1])

		for i in x:
			i = float(i)
		for j in y:
			j = float(j)

	else:
		return None

	plt.plot(x, y, color='k', ls='-', lw='2')
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)

	plt.savefig("sciencefrontend/static/img/picplot.png")
	plt.savefig("sciencefrontend/static/img/picplot.pdf")
	plt.savefig("sciencefrontend/static/img/picplot.svg")

	
	return HttpResponse("/static/img/picplot")