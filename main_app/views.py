from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from health_record.models import HealthRecord


# Create your views here.

def home(request):
    """
    Home page view
    """
    if request.user.is_authenticated is False:
        return render(request, 'login.html')

    health_records = HealthRecord.objects.all()

    return render(request, 'home.html', {'health_records': health_records})

def do_login(request):
    """
    Login page view
    """
    if request.user.is_authenticated:
        return render(request, 'home.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        auth_user = authenticate(request, username=username, password=password)

        if auth_user is not None:
            login(request, auth_user)
            request.session['success'] = 'Đăng nhập thành công!'
            return redirect('home')
        else:
            request.session['error'] = 'Sai tài khoản hoặc mật khẩu!'
            return redirect('login')

    return render(request, 'login.html')

def do_logout(request):
    """
    Logout page view
    """
    if request.user.is_authenticated is False:
        return render(request, 'login.html')

    logout(request)
    request.session['success'] = 'Đăng xuất thành công!'
    return redirect('login')