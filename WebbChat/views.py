from django.http import response, HttpResponse
from django.shortcuts import render
from .models import User

from WebbChat.forms import FormLogin
from WebbChat.forms import FormRegister


def index(request):
    """
    Describe: load list user
    :param request:
    :return:
    """
    list_friends = User.objects.all()
    context = {
        'friends': list_friends
    }
    return render(request, "home/index.html", context)


def login(request):
    """
    Describe :xu li dang nhap
    :param request:
    :return:
    """
    form = FormLogin()
    if request.method == 'POST':
        form = FormLogin(request.POST)
        if form.is_valid():
            if form.logged() >= 1:
                return HttpResponse('dang nhap thanh cong')
            else:
                return HttpResponse('that bai')
    return render(request, 'home/index.html', {'form': form})


def register(request):
    """
    Describe: xu li dang ki
    :param request:
    :return:
    """
    form = FormRegister()
    if request.method == 'POST':
        form = FormRegister(request.POST)
        if form.is_valid():
            form.save_user()
            return HttpResponse('')
    return render(request, "home/index.html", {'form': form})

# Create your views here.
