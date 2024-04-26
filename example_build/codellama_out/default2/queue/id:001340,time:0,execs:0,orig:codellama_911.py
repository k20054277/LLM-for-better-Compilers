from django.shortcuts import render

def my_view(request):
    if request.method == 'POST' and request.POST['name']:
        # Do something with the name field in the POST data
        pass
    else:
        # Do something else
        pass