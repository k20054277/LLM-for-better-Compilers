
# Import necessary libraries
from django.urls import path
from django.shortcuts import render

# Define the main function
def home(request):
    # Return a template
    return render(request, 'home.html')

# Define the URL patterns
urlpatterns = [
    path('home/', home)
]
