from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def profile(request):
    current_user = request.user
    print (current_user.userid)
    context = {
        "userid": current_user.userid,
        "username": current_user.username,
    }
    return render(request, 'profile.html', context)