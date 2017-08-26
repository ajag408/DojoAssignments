from django.shortcuts import render
from forms import RegisterForm
# Create your views here.
def index(request):
    form = RegisterForm() # We will build this class out in just a minute
    context = {
    	'myregistrationform': form # Form is the variable name referencing the instance of our RegistrationForm class
    }
    return render(request, 'regForm/reg.html', context)


def register(request):
  # Confirm that the HTTP verb was a POST
    if request.method == "POST":
# Bind the POST data to an instance of our RegisterForm
        bound_form = RegisterForm(request.POST)
        # Now test that bound_form using built-in methods!
        # *************************
        print bound_form.is_valid() # True or False, based on the validations that were set!
        print bound_form.errors # Any errors in this form as a dictionary
        # *************************
    return redirect('/')
