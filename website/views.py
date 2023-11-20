from django.shortcuts import render, redirect, get_object_or_404

from website.forms import AddPostForm
from website.models import *


def index(request):
    questionnaires = Person.objects.all()
    return render(request, 'website/index.html', {'title': 'Главная страница', 'questionnaires': questionnaires})


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'website/addpage.html', {'form': form, 'title': 'Добавление анкеты'})

