
# Import necessary libraries
from django.shortcuts import render

# Define the main function
def home(request):
    # Return a render template
    return render(request, 'home.html')

# Define the main URL pattern
urlpatterns = [
    path('home/', home),
]
