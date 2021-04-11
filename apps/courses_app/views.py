from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    context = {
    'courses' : Courses.objects.all()
    }
    return render(request, "index.html", context)

def add(request):
    errors = Courses.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        Courses.objects.create(course_name=request.POST['course_name'], description=request.POST['description'])
    messages.success(request, "Show successfully created")
    return redirect('/')


def remove(request, id):
    context = {
        'course' : Courses.objects.get(id=id)
    }
    return render(request, 'remove.html', context)

def delete(request, id):
    Courses.objects.get(id=id).delete()
    return redirect('/')