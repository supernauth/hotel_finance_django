from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from hotel_finance.models import Type, Room

def index(request):
    rooms = Room.objects.all()
    return HttpResponse(loader.get_template('index.html').render({
        'room_types': Type.objects.all(),
        'rooms': rooms,
        'income': 3 # ide kell majd az összegzés
    }, request))    

def add_type(request):
    return HttpResponse(loader.get_template('type.html').render({}, request))

def add_type_record(request):
    Type(name=request.POST.get('name'), suite=request.POST.get('suite') == 'on').save()
    return HttpResponseRedirect(reverse('index'))

def update_type(request, id):
    return HttpResponse(loader.get_template('type.html').render({'type': Type.objects.get(id=id)}, request))

def update_type_record(request, id):
    type = Type.objects.get(id=id)
    type.name = request.POST.get('name')
    type.suite = request.POST.get('suite') == 'on'
    type.save()
    return HttpResponseRedirect(reverse('index'))

def delete_type(request, id):
    Type.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('index'))


def add_room(request):
    return HttpResponse(loader.get_template('room.html').render({
        'room_types': Type.objects.all(),
    }, request))
    
def add_room_record(request):
    Room(
        name=request.POST.get('name'),
        has_views=request.POST.get('has_views') == 'on',
        type=Type.objects.get(id=request.POST.get('type_id'))
    ).save()
    return HttpResponseRedirect(reverse('index'))

def update_room(request, id):
    return HttpResponse(loader.get_template('room.html').render({
        'room': Room.objects.get(id=id),
        'room_types': Type.objects.all()
    }, request))
    
def update_room_record(request, id):
    room = Room.objects.get(id=id)
    room.name = request.POST.get('name')
    room.has_views = request.POST.get('has_views') == 'on'
    room.night_count = request.POST.get('night_count')
    room.type = Type.objects.get(id=request.POST.get('type_id'))
    room.save()
    return HttpResponseRedirect(reverse('index'))

def delete_room(request, id):
    Room.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('index'))
    