from django.shortcuts import render
from .models import *

def film_list(request):
    films = Film.objects.all()
    return render(request, 'films/film_list.html', {'films': films})

def chose_film(request, film_id):
    film = Film.objects.get(id=film_id)
    all_seances = Seance.objects.filter(film_connection=film_id)
    return render(request, 'films/chose_film.html', {'film': film, 'all_seances': all_seances})


def seance(request, seance_id):
    hall = Hall.objects.filter()
    return render(request, 'films/seance.html', {'hall': hall})

def ticket(request):
    ticket = Ticket.objects.filter()
    return render(request, 'films/ticket.html', {'ticket': ticket})

