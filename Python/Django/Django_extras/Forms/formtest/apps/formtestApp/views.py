from django.shortcuts import render
from forms import RegistrationForm
# Create your views here.
def index(request):
    form = RegistrationForm() # We will build this class out in just a minute
    context = {
    	'myregistrationform': form # Form is the variable name referencing the instance of our RegistrationForm class
    }
    return render(request, 'formtestApp/index.html', context)
