from django.contrib.auth import login, authenticate
from django.shortcuts import get_object_or_404, render, redirect

from .forms import RegisterForm, FilterTeacherForm
from .models import Subject, Teacher


def index(request):
    if request.method == 'POST':
        form = FilterTeacherForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            subject = form.cleaned_data.get('subject')
            teachers = Teacher.objects
            if subject != 0:
                teachers = teachers.filter(subjects__id=subject)
            if first_name != 'all':
                teachers = teachers.filter(first_name__startswith=first_name)
            if last_name != 'all':
                teachers = teachers.filter(last_name__startswith=last_name)

            return render(
                request,
                "index.html",
                {"teachers": teachers.all(), "form": form}
            )

    form = FilterTeacherForm()
    teachers = Teacher.objects.all()
    return render(request, "index.html", {"teachers": teachers, "form": form})


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
