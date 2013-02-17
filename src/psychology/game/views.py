# Create your views here.
from django.shortcuts import render_to_response
from psychology.game.models import Level, Hint

def level(request, level_id):
    o = Level.objects.get(id=level_id)

    values = {
    'level':o
    }

    return render_to_response('level.html', values)

def hint(request, hint_id):
    
#    clicked = hints.pk from website
    
    hint = Hint.objects.get(id=hint_id)
    
    values = {
              'hint':hint
              }
    
    return render_to_response('hint.html', values)