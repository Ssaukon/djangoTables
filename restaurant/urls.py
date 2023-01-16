from django.urls import path
# from restaurant import views
 
from .views import restaurant_tables

 
urlpatterns = [
    path('', restaurant_tables, name='index'),
   
]