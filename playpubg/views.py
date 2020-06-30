from django.shortcuts import render
from matches.models import Match

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def live(request):
    try:
        live = Match.objects.get(match_status="running")
    except:
        live = None
    if live:
        context = {"match":live}
    else:
        context = {"match":"no_match"}
    return render(request, 'live.html', context)

def top_players(request):
    return render(request, 'top_players.html')

def rules(request):
    return render(request, 'rules.html')

