# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from psychology.game.models import Level, Hint
import json


def game(request):
    # loads the game into the game.html, starts at level 1
    
    values = {
              'level':1,
    }
    return render_to_response('game.html', values)

def level(request, level_id):
    # loads the requested level
    
    o = Level.objects.get(id=level_id)

    values = {
    'level':o,
    }
    
    return render_to_response('level.html', values)

def hint(request, hint_id):
    # loads the requested hint 
    
    hint = Hint.objects.get(id=hint_id)
    
    values = {
              'hint':hint
              }
    
    return render_to_response('hint.html', values)


def answer(request, level_id):
    # checks the guess and returns whether the guess was True or False

    o = Level.objects.get(id=level_id)

    guess = request.GET.get('guess', '').strip()
    correct = o.answers.filter(value__iexact=guess).exists()
           
    return HttpResponse(json.dumps(correct), content_type="application/json")


