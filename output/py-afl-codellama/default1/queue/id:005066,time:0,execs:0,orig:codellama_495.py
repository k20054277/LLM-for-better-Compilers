from django.http import HttpResponse

def my_view(request):
    # Check if the user has provided a value for the "name" parameter
    if request.GET.get('name') is None:
        return HttpResponse("Please provide a value for 'name'")

    # Use the value of the "name" parameter to create a greeting message
    name = request.GET['name']
    message = f"Hello, {name}!"

    # Return the greeting message as an HTTP response
    return HttpResponse(message)