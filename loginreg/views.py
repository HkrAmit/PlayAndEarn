from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.utils.crypto import get_random_string
from .forms import UserLoginForm, UserRegForm, UserVerifyForm
from accounts.models import MyUser
from .models import players, temp_player

# Create your views here.
def user_login(request):
    if request.user.is_authenticated:
        return redirect("profile")
    forms = UserLoginForm()
    if request.method == 'POST':
        forms = UserLoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data["username"]
            password = forms.cleaned_data["password"]
            #print(username, password)

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                context = {'forms':forms, "error":"Incorrect Username or Password"}
                return render(request, 'login.html', context)


    context = {'forms':forms}
    return render(request, 'login.html', context)

def user_logout(request):
    logout(request)
    return redirect('home')

def resend_otp(request, session):
    try:
        temp_user = temp_player.objects.get(session=session)
        print (temp_user.otp2)
        if temp_user.otp2 == None:
            otp = get_random_string(length=6, allowed_chars="1234567890")
            print (otp)
            temp_user.otp2 = otp
            temp_user.save()
        elif temp_user.otp3 == None:
            otp = get_random_string(length=6, allowed_chars="1234567890")
            print (otp)
            temp_user.otp3 = otp
            temp_user.save()
        else:
            pass
    except:
        return redirect('home')
    return redirect('verify', session=session)

def velidate_otp(request, session):
    # if request.user.is_authenticated:
    #     return redirect("home")
    
    forms = UserVerifyForm()

    try:
        data = temp_player.objects.get(session=session)
        #print(data.name)
        if request.method == 'POST':
            forms = UserVerifyForm(request.POST)
            if forms.is_valid():
                otp = forms.cleaned_data["otp"]
                print(otp, data.otp2)
                if otp == data.otp:
                    name = data.name
                    pubg_name = data.pubg_name
                    pubg_id = data.pubg_id
                    mobile = data.mobile
                    email = data.email
                    password = data.password
                    print("Got user data")

                    user_obj = MyUser.objects.create_user(mobile=mobile, userid=pubg_id, password=password, username=pubg_name)
                    new_user = players.objects.create(
                        user=user_obj,
                        name=name,
                        pubg_name=pubg_name,
                        pubg_id=pubg_id,
                        mobile=mobile,
                        email=email,
                    )
                    print("User Created")
                    data.delete()
                    user = authenticate(username=mobile, password=password)
                    login(request, user)
                    return redirect("profile")
                    
                else:
                    context = {'forms':forms, 'user':session, 'error':'OTP not matched'}
                    return render(request, "verify.html", context)

        context = {'forms':forms, 'user':session}
        return render(request, "verify.html", context)

    except:
        return redirect('home')
    


def register(request):
    if request.user.is_authenticated:
        return redirect("profile")

    forms = UserRegForm()

    if request.method == 'POST':
        forms = UserRegForm(request.POST)
        print(forms)
        print(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            pubg_name = forms.cleaned_data['pubg_name']
            pubg_id = forms.cleaned_data['pubg_id']
            mobile = forms.cleaned_data['mobile']
            email = forms.cleaned_data['email']
            password = forms.cleaned_data['re_password']
            otp = get_random_string(length=6, allowed_chars="1234567890")
            print (otp)
            session = get_random_string(length=10, allowed_chars="1234567890")

            temp_player.objects.create(
                name=name,
                pubg_name=pubg_name,
                pubg_id=pubg_id,
                mobile=mobile,
                email=email,
                password=password,
                otp=otp,
                session=session
            )

            return redirect('verify', session=session)

    context = {'forms': forms}
    return render(request, 'register.html', context)


