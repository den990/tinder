from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'users/index.html')

def profile(request):
    return render(request, 'users/profile_screen.html')

def login(request):
    return render(request, 'users/login_screen.html')

def registration(request):
    return render(request, 'users/registration_screen.html')

def notification(request):
    return render(request, 'users/notification_screen.html')

def recommendations(request):
    return render(request, 'users/recommendations_screen.html')

def message(request):
    return render(request, 'users/message_screen.html')
