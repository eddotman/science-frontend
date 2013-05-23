from django.shortcuts import render

def function_plot(request):

	script_name = "function_plot.py"
	script_link = "https://github.com/eddotman/science-frontend/blob/master/sciencefrontend/scripts/function_plot.py"

	script_gui = echo_function_plot_content()

	return render(request, 'home.html', {'script_name': script_name, 'script_link': script_link, 'script_gui': script_gui})

def echo_function_plot_content():
	content = """
			<h1>function_plot.py</h1>
			<pre><strong>function_plot.py</strong> will convert an uploaded data file (containing two columns of x and y data) into a high-quality graph (PNG + PDF).</pre>
			<hr>
			<h2>Please upload a data file</h2>
			<p>(Format: two columns of floating-point numbers; first row should be [x,y] labels.)</p>
			<input type=\"file\" title=\"Upload a data file...\">
			<hr>
			<h3>Example: Data file format</h3>
			<pre>
			x                 y
			1                 1.0
			2                 4.0
			3                 9.0
			.                 .
			.                 .
			.                 .
			</pre>
			"""
	return content

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