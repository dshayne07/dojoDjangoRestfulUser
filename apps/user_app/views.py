from django.shortcuts import render, redirect
from django.contrib import messages
from models import *

def index(request):
    context = {
        'users':User.objects.all()
    }
    return render(request, 'user_app/index.html', context)

def show(request, user_id):
    context = {
        'data':User.objects.get(id=user_id)
    }
    return render(request, 'user_app/show.html', context)

def add(request):
    return render(request, "user_app/add.html")

def edit(request, user_id):
    context = {
        'data':User.objects.get(id=user_id)
    }
    return render(request, 'user_app/edit.html', context)

def update(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/'+request.POST['user_id']+'/edit')
    else:
        b = User.objects.get(id=request.POST['user_id'])
        b.first_name = request.POST['first_name']
        b.last_name = request.POST['last_name']
        b.email = request.POST['email']
        b.save()
    return redirect('/users/'+request.POST['user_id'])

def destroy(request, user_id):
    print User.objects.get(id=user_id).delete()
    return redirect('/users/')

def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/add/')
    else:
        User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'])
    return redirect('/users/')