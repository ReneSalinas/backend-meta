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
    about_content = {'about': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12- 15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."} 
    return render(request, 'about.html', {'content': about_content})

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