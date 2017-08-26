from django.shortcuts import render
from django.contrib.auth.models import User
import random
def index(request):
  User.objects.create_user(first_name="Mike", last_name="Hannon", username=str(random.randint(0,100)))
  # Creating a random string as an arbitrary username, since usernames must be unique
  users = User.objects.all() #retrieves all users
  return render(request, 'testUser/index.html', {'users': users})
