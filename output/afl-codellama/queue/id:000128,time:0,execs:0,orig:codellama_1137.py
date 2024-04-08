# Create a new Django project
$ django-admin startproject myproject

# Change directory into the project
$ cd myproject

# Add a new app to the project
$ python manage.py startapp myapp

# Define some views in the app
$ echo 'from django.shortcuts import render' >> myapp/views.py
$ echo 'def home(request):' >> myapp/views.py
$ echo '    return render(request, "home.html")' >> myapp/views.py

# Define a template for the home view
$ echo '<h1>Home Page</h1>' > myproject/templates/home.html

# Add the app to the project's settings file
$ echo 'INSTALLED_APPS = [' >> myproject/settings.py
$ echo '    "myapp",' >> myproject/settings.py
$ echo ']' >> myproject/settings.py