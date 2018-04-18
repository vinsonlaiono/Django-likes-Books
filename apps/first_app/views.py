from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, "first_app/index.html", context)


