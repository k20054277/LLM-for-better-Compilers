
from django.http import HttpResponse

def my_view(request):
    # This variable will not be assigned a value
    # and it will have the value of None
    my_variable = None

    if request.method == 'POST':
        # Here you can assign a value to `my_variable`
        # for example, when form data is submitted
        my_variable = request.POST.get('mykey')

    if my_variable is not None:
        return HttpResponse(f"Received value: {my_variable}")

    return HttpResponse("No value received")
