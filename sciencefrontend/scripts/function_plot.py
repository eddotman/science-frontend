from django.shortcuts import render

def function_plot(request):
	import os

	name = "function_plot"

	script_name = name + ".py"
	script_link = "https://github.com/eddotman/science-frontend/blob/master/sciencefrontend/scripts/" + name + ".py"

	html_content = open(os.path.dirname(__file__) + "\\html_content\\" + name + ".html")
	script_gui = html_content.read()

	return render(request, 'home.html', {'script_name': script_name, 'script_link': script_link, 'script_gui': script_gui})

def function_plot_image(request, type):
	from numpy import *
	import matplotlib.pyplot as plt
	from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
	from matplotlib.figure import Figure
	from django.http import HttpResponse

	fig = Figure(facecolor=(1,1,1))
	ax = fig.add_subplot(111)

	x = arange(0, 10, 0.1)
	datax = x
	datay = sin(x)

	ax.plot(datax, datay, color='k', ls='-', lw='2.5')
	#ax.set_xlim(float(xmin), float(xmax))
	#ax.set_ylim(float(ymin), float(ymax))
	#ax.set_xlabel(xlabel)
	#ax.set_ylabel(ylabel)

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