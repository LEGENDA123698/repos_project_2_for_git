from django.shortcuts import render,redirect
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth import login, authenticate


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("film-list")
    else:
        form = UserCreationForm()
        
    return render(request, 'register/register.html', {'form': form})

