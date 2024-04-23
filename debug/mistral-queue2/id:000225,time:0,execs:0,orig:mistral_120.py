
# Python boolean value - False
is_subscribed = False
print(is_subscribed)  # Output: False

if not is_subscribed:
    print("You are not subscribed.")
else:
    print("Welcome subscriber!")

# Django example using the False boolean value in a view and template context
from django.http import HttpResponse

def home(request):
    is_subscribed = False
    context = {'is_subscribed': is_subscribed}
    if not is_subscribed:
        return HttpResponse("You are not subscribed.")
    else:
        return HttpResponse("Welcome subscriber!")
