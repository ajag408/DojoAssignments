from django.shortcuts import render
from django.views.generic import View
# Create your views here.
class ExampleView(View):
  footerText = "Fake Copyright 2016, Blob the Blob"
  def get(self,request):
    context = {
    'footer':self.footerText
    }
    return render(request, 'testApp/index.html', context)
class ExtendExample(ExampleView):
  footerText = "Fake Copyright 2017"
