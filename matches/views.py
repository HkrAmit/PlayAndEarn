from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.apps import apps
from . import models
from .models import Match_1_Player
from .forms import MatchRegFormDirect, MatchRegFormBkash


# Create your views here.
def matches(request):
    all_matches = models.Match.objects.all()
    context = {
        'matches': all_matches,
        'set_one': [1,2,3],
        'set_two':[4,5,6]
    }
    return render(request, 'matches.html', context)

def reg_for_match(request, match_id):
    details = models.Match.objects.get(id=match_id)
    
    reg_match = apps.get_model('matches',"Match_"+str(match_id)+"_Player")

    registered_users = reg_match.objects.values_list('playerid')
    for user in registered_users:
        if int(request.user.userid) in user:
            return redirect('profile')

    forms1 = MatchRegFormDirect()
    forms2 = MatchRegFormBkash()

    if request.method == 'POST':
        if request.POST.get("txnid"):
            forms2 = MatchRegFormBkash(request.POST)
            if forms2.is_valid():
                txnid = forms2.cleaned_data['txnid']
                password = forms2.cleaned_data['re_password']

                if not check_password(password, request.user.password):
                    context = {'match':details, 'forms1':forms1, 'forms2':forms2, 'error2':'Incorrect Password'}
                    return render(request, 'reg_for_match.html', context)
                
                reg_match.objects.create(
                    playerid = request.user.userid,
                    playername = request.user.username,
                    paid_through = 'bkash',
                    txnid = txnid
                )

        else:
            forms1 = MatchRegFormDirect(request.POST)
            if forms1.is_valid():
                password = forms1.cleaned_data['re_password']

                if not check_password(password, request.user.password):
                    context = {'match':details, 'forms1':forms1, 'forms2':forms2, 'error1':'Incorrect Password'}
                    return render(request, 'reg_for_match.html', context)

                reg_match.objects.create(
                    playerid = request.user.userid,
                    playername = request.user.username,
                    paid_through = 'account'
                )

    context = {'match':details, 'forms1':forms1, 'forms2':forms2}
    return render(request, 'reg_for_match.html', context)