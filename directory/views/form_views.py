from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from ..forms import (
    SubjectCreationForm,
    TeacherCreationForm,
    TeacherImportForm,
    RegisterForm)


@login_required
def subject_add(request):
    if request.method == 'POST':
        form = SubjectCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('directory:index')
        else:
            return render(request, "subject-add.html", context={"form": form})

    form = SubjectCreationForm()
    return render(request, "subject-add.html", {"form": form})


@login_required
def teacher_add(request):
    if request.method == 'POST':
        form = TeacherCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('directory:index')
        else:
            return render(request, "teacher-add.html", context={"form": form})

    form = TeacherCreationForm()
    return render(request, "teacher-add.html", {"form": form})


@login_required
def teacher_bulk_add(request):
    if request.method == 'POST':
        form = TeacherImportForm(request.POST, request.FILES)
        if form.is_valid():
            return redirect('directory:index')
        else:
            return render(request, 'teacher-import.html', {'form': form})
    form = TeacherImportForm()
    return render(request, 'teacher-import.html', {'form': form})


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
