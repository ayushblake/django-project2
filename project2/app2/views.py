from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#def home(request):
#    return HttpResponse("<em>This text is in the home function in views.py</em>")
def demo(request):
    return HttpResponse("<strong>This text is in the demo function in views.py</strong>")
def home(request):
     my_dict = {'insert_me':"Now I am coming from first_app/home.html!"}
     # Make sure this is pointing to the correct index
     return render(request,'app2/home.html',context=my_dict)
