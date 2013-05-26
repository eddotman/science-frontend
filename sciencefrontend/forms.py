from django import forms

class FunctionPlotForm(forms.Form):
    datafile = forms.FileField(label=u'Please upload a data file...')