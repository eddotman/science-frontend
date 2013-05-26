from dajaxice.utils import deserialize_form
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

@dajaxice_register
def send_form(request, form):
    dajax = Dajax()
    form = FunctionPlotForm(deserialize_form(form))

    if form.is_valid():
        dajax.remove_css_class('#data_form datafile', 'error')
        dajax.alert("Uploaded file is: %s" % form.cleaned_data.get('datafile'))
    else:
        dajax.remove_css_class('#data_form datafile', 'error')
        for error in form.errors:
            dajax.add_css_class('#id_%s' % error, 'error')

    return dajax.json()