from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, OrderForm
from .models import User
from django.contrib.auth.hashers import make_password, check_password

def home(request):
    return render(request, 'main/home.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Это имя пользователя уже занято. Пожалуйста, выберите другое или нажмите "Вход".')
            else:
                password = make_password(form.cleaned_data['password'])
                user = User(username=username, password=password)
                user.save()
                return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'main/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(username=username)
                if check_password(password, user.password):
                    # Логика аутентификации пользователя
                    return redirect('home')
                else:
                    form.add_error('password', 'Неправильный пароль')
            except User.DoesNotExist:
                form.add_error('username', 'Пользователь не найден')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})

def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Логика обработки заказа
            return redirect('home')
    else:
        form = OrderForm()
    return render(request, 'main/order.html', {'form': form})


def order_success(request):
    return render(request, 'main/order_success.html')
