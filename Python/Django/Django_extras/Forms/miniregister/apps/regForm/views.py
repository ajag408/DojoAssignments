from django.shortcuts import render, redirect
from forms import RegisterForm
from .models import User
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
        if bound_form.is_valid() is True:
            User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = request.POST['password'], confirm_password = request.POST['confirm_password']) # True or False, based on the validations that were set!
        print bound_form.errors # Any errors in this form as a dictionary
        # *************************
    return redirect('/')
