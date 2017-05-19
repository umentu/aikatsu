from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import MusicList

# Create your views here.
def index(request):
    template = loader.get_template('sites/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def music_list(request):

    music_list = MusicList.objects.order_by('-numbering')
    template = loader.get_template('sites/music_list.html')
    context = {
        'music_list': music_list,
    }

    return HttpResponse(template.render(context, request))