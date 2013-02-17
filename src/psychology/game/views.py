# Create your views here.
from django.shortcuts import render_to_response
from psychology.game.models import Level

def level(request, level_id):
    o = Level.objects.get(id = level_id)

    values = {
    'level':o
    }

    return render_to_response('level.html', values)