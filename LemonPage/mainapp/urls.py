from django.urls import path 
from . import views 

urlpatterns = [ 
    path('', views.index, name='index'), 
    path('homepage/', views.homepage, name="homepage"),
    path('display-date', views.display_date, name='display'),
    path('drinks/<str:drink_name>',views.drinks,name="drink_name"),
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),
    path('book/', views.book, name="book"),
    path('booking/', views.form_view, name="booking")
] 