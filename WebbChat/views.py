from django.http import response, HttpResponse
from django.shortcuts import render
from .models import User
from Utils import utils

from WebbChat.forms import *


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
            # print(form.cleaned_data['name'])
            # print(form.cleaned_data['password'])
            user = User.objects.filter(
                name=form.cleaned_data['name'], password=utils.hashlib_md5(form.cleaned_data['password'])).first()
            if not user:
                return HttpResponse('ko thanh cong')
            else:
                list_friends = User.objects.filter(course=user.course)
                user_logged = {
                    'list_friends': list_friends,
                    'users': user.name
                }
                return render(request, 'home/friends.html', user_logged)
    # print('a = ', request.GET.get('a'))
    # print('b = ', request.GET.get('b'))
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


def details(request):
    form = FormManger()
    if request.method == 'POST':
        form = FormLogin(request.POST)
        if form.is_valid():
            pass

# Create your views here.
