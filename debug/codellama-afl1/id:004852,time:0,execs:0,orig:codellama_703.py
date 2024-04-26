# Import the Django module
from django import template

# Define a template tag
@register.simple_tag(takes_context=True)
def my_tag(context):
    # Access the current request object
    request = context['request']
    
    # Use the request object to get the user's IP address
    ip_address = request.META['REMOTE_ADDR']
    
    # Return a boolean value based on whether or not the IP address is in the allowed list
    return ip_address in ['192.168.0.1', '192.168.0.2']