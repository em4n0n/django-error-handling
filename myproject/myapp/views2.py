# Consider the following scenario, where you have a Product model in the app. 

# The user wants the details of a product with a specific Product ID. 

# In the following view function, id is the parameter obtained from the URL. 

# It tries to determine whether any product with the given id is available. If not, the Http404 exception is raised.

from django.http import http404, HttpResponse
from .models import Product

def detail(request, id):
    try:
        p = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return HttpResponse("Product Found")

# FieldDoesNotExist: This exception is raised when the requested field does not exist.

try:
    field = model._meta.get_field(field_name)
except FieldDoesNotExist:
    return HttpResponse("Field does not exist")

# PermissionDenied: This exception is raised when a user does not have permission to perform the action requested.

def myview(request):
    if not request.user.has_perm('myapp.view_mymodel'):
        raise PermissionDenied()
    return HttpResponse()