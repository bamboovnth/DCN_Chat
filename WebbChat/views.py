from django.http import response, HttpResponse
from django.shortcuts import render
from .models import User

from WebbChat.forms import FormLogin
from WebbChat.forms import FormRegister


def index(request):
    list_friends = User.objects.all()
    context = {
        'friends': list_friends
    }
    return render(request, "home/index.html", context)


def login(request, name, password):
    if request.method == 'POST':
        pass


def register(request):
    form = FormRegister()
    if request.method == 'POST':
        form = FormRegister(request.POST)
        if form.is_valid():
            form.save_user()
            return HttpResponse('/admin')
    return render(request, "home/index.html", {'form': form})

# Create your views here.
