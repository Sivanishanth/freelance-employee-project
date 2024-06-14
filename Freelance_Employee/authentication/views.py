
from django.shortcuts import render
from django.template import loader
from .form import Client_Register,Freelance_Register,Teac_Team

from django.http import HttpResponse,HttpResponseRedirect

def auth(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        CR = Client_Register(request.POST)
        FR = Freelance_Register(request.POST)
        TT = Teac_Team(request.POST)
        # check whether it's valid:
        # if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return HttpResponseRedirect("")

    # if a GET (or any other method) we'll create a blank form
    else:
        CR = Client_Register()
        FR = Freelance_Register()
        TT = Teac_Team()

    return render(request, "main.html", {"Client_Register": CR,"Tech_Team":TT,"Freelance_Register":FR})

