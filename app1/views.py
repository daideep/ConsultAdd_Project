
from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.

# def home(request):
#     return HttpResponse("Hello, world <a href='/app/show/'>Click Here</a>")

# def show(request):
#     return HttpResponse("<h1>Show Page</h1>")

def home(request):
    return render(request,"index.html")

def form(request):
    form = forms.Registerform

    if request.method == "POST":
        form = forms.Registerform(request.POST)
        if form.is_valid():
            print("Validation Worked")
            print("name :" + form.cleaned_data['name'])
            print("email :" + form.cleaned_data['email'])
            print("confirm_email :" + form.cleaned_data['confirm_email'])
            print("text :" + form.cleaned_data['text'])

    return render(request, 'register.html', {'form':form})




