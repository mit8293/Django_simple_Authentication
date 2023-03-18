from django.shortcuts import render

# new imports
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

# Create your views here.


def frontend(request):
    return render(request, 'test_app/frontend.html')


@login_required(login_url="/login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def backend(request):
    return render(request, 'test_app/single.html')

##################################
# Login Function


def Login(request):
    if request.user.is_authenticated:
        return render(request, "test_app/single.html")
    else:
        messages.info(request, "Please login to access this page.")
        return HttpResponseRedirect('/')

# Login User


def LoginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user != None:
            login(request, user)
            return HttpResponseRedirect("/backend")
        else:
            messages.error(request, "Enter your data correctly.")
            return HttpResponseRedirect("/")

# LogoutUser function


def LogoutUser(request):
    logout(request)
    request.user = None
    return HttpResponseRedirect("/")


# test page
# def log(request):
#     return render(request, "test_app/login_test.html")
