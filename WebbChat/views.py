from django.shortcuts import render
from .models import User


def index(request):
    list_friends = User.objects.all()
    context = {
        'friends': list_friends
    }

    return render(request, "home/index.html", context)




# Create your views here.
