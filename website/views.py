from django.shortcuts import render, redirect

from website.forms import AddPostForm
from website.models import *


def index(request):
    tags = Tag.objects.all()
    questionnaires = Person.objects.all()
    return render(request, 'website/index.html', {'tags': tags, 'questionnaires': questionnaires})


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'website/addpage.html', {'form': form, 'title': 'Добавление анкеты'})
