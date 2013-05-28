from script_base import ScriptBase

def function_plot(request):
	from django.shortcuts import render

	s = ScriptBase("function_plot")

	return render(request, 'home.html', {'script_name': s.script_name,  'js_link': s.js_link, 'script_link': s.script_link, 'script_gui': s.script_gui})

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

def function_plot_submit(request):
	from django.http import HttpResponse

	a = "test"
	return HttpResponse(a)