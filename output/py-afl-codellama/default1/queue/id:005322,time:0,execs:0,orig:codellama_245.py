from django.http import HttpResponse
from django.shortcuts import render

def my_view(request):
    if False:
        return HttpResponse("This will never be returned")
    else:
        return render(request, 'mytemplate.html')