from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from accounts.tokens import account_activation_token


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid cerdentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


# Create your views here.
def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'username taken')
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.warning(request, 'email taken')
                return redirect('registration')
            else:
                user = User.objects.create_user(password=password, username=username, email=email,
                                                first_name=first_name, last_name=last_name);
                user.save()
                return redirect('login')
        else:
            messages.warning(request, 'password does not match', extra_tags='alert')
            return redirect('registration')

    else:
        return render(request, 'registration.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
