from django.contrib import auth, messages
from django.http import request
from django.shortcuts import render, redirect

# Create your views here.
from register.models import register


def registration(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('psw')
        password2 = request.POST.get('psw-repeat')
        secques = request.POST.get('sq')
        secans = request.POST.get('ans')
        prflanguage = request.POST.get('pl')
        gender = request.POST.get('gender')
        first_name = request.POST.get('fname')
        mid_name = request.POST.get('mname')
        last_name = request.POST.get('lname')
        dofbir = request.POST.get('birth')
        occupation = request.POST.get('occu')
        maritalstatus = request.POST.get('ms')
        countryname = request.POST.get('cname')
        mobileno = request.POST.get('mno')
        nationality = request.POST.get('nname')
        doorno = request.POST.get('message')
        street = request.POST.get('message1')
        Area = request.POST.get('message2')
        pincode = request.POST.get('pin')
        state = request.POST.get('state')
        town = request.POST.get('city')
        postoffice = request.POST.get('post')
        phoneno = request.POST.get('phone')
        ResitoOffAddr = request.POST.get('radd')
        if password == password2:
            if register.objects.filter(email=email).exists():
                messages.warning(request, 'email is  taken')
                return redirect('registration')
            else:
                user = register(email=email, password=password, secques=secques, secans=secans,
                                prflanguage=prflanguage, gender=gender, first_name=first_name,
                                last_name=last_name, dofbir=dofbir, occupation=occupation,
                                maritalstatus=maritalstatus, countryname=countryname,
                                mobileno=mobileno, nationality=nationality, doorno=doorno,
                                street=street, Area=Area, pincode=pincode, state=state, town=town,
                                postoffice=postoffice, phoneno=phoneno,
                                ResitoOffAddr=ResitoOffAddr, mid_name=mid_name);
                user.save()
                return redirect('login')
        else:
            messages.warning(request, 'password does not match', extra_tags='alert')
            return redirect('registration')

    else:
        return render(request, 'registration.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = register.objects.filter(email=username, password=password).exists()
        if user :
            return render(request, 'main.html')
        else:
            messages.info(request, 'invalid cerdentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout():
    pass
