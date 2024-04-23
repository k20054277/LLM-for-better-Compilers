from django.http import HttpResponse

def my_view(request):
    # Assert that the request has a 'name' parameter
    assert 'name' in request.GET, "Missing 'name' parameter"
    
    name = request.GET['name']
    
    # Return an HTTP response with the user's name
    return HttpResponse(f"Hello, {name}!")