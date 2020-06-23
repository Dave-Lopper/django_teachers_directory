from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from .forms import RegisterForm
from .models import Subject, Teacher


def index(request):
    teachers = Teacher.objects.all()
    return render(request, "index.html", {"teachers": teachers})


def teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    print(teacher, teacher.subjects)
    return render(request, 'teacher.html', {'teacher': teacher})


def subject(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    return render(request, 'subject.html', {'subject': subject})


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('directory:index')
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form': form})
