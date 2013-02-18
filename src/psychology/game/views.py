# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
<<<<<<< HEAD
from psychology.game.models import Level, Hint
import json


def game(request):
    return render_to_response('game.html')


def level(request, level_id):
    o = Level.objects.get(id=level_id)
    correct=""
    
    guess = request.GET.get('guess', '')
    correct = o.answers.filter(value=guess).exists()
           
    values = {
    'level':o,
    'correct': correct,
    'guess' : guess,
   
    
=======
from psychology.game.models import Level, Hint, Answer

def level(request, level_id):
    o = Level.objects.get(id=level_id)

    
    guess = request.GET.get('guess', '')
    correct = o.answers.filter(value=guess).exists()
        
    values = {
    'level':o,
    'correct':correct,
    'guess':guess,
>>>>>>> de2be314ef356ce85b944916093292209bcfaab1
    }
    
    return render_to_response('level.html', values)

def hint(request, hint_id):
    
#    clicked = hints.pk from website
    
    hint = Hint.objects.get(id=hint_id)
    
    values = {
              'hint':hint
              }
    
    return render_to_response('hint.html', values)

<<<<<<< HEAD

def answer(request, level_id):
    o = Level.objects.get(id=level_id)

    guess = request.GET.get('guess', '')
    correct = o.answers.filter(value=guess).exists()
           
    return HttpResponse(json.dumps(correct), content_type="application/json")
=======
>>>>>>> de2be314ef356ce85b944916093292209bcfaab1
