from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from datetime import datetime
from mainapp.forms import BookingForm

def index(request): 
    return HttpResponse("Hello, world. This is the index view of mainapp.") 

def homepage(request):
    return HttpResponse("ISAAAAAC PROJECT IS REAL")

def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)

def drinks(request, drink_name):
    drinks = {
        'mocha':"type of coffee",
        'tea':"type of beverage",
        'lemonade':"type of refreshment"                
    }    
    choice_of_drink = drinks[drink_name]
    return HttpResponse(f"<h2> {drink_name} </h2>" + choice_of_drink)

def home(request):
    return HttpResponse("Welcome to Little Lemon!")

def about(request):
    return HttpResponse("About us")

def menu(request):
    return HttpResponse("Menu")

def book(request):
    return HttpResponse("Make a booking")

def form_view(request):
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form":form}
    return render(request, "booking.html", context)