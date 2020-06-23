from django.shortcuts import render

from ..forms import TeacherFilterForm
from ..models import Subject, Teacher


def index(request):
    if request.method == 'POST':
        form = TeacherFilterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            subject = form.cleaned_data.get('subject')
            print(last_name, first_name, subject)
            teachers = Teacher.objects
            if subject != "0":
                print(1)
                teachers = teachers.filter(subjects__id=subject)
            if first_name != 'all':
                print(2)
                teachers = teachers.filter(first_name__startswith=first_name)
            if last_name != 'all':
                print(3)
                teachers = teachers.filter(last_name__startswith=last_name)
            return render(
                request,
                "index.html",
                {"teachers": teachers.all(), "form": form}
            )

    form = TeacherFilterForm()
    teachers = Teacher.objects.all()
    subjects = Subject.objects.all()
    return render(
        request,
        "index.html",
        {"subjects": subjects, "teachers": teachers, "form": form}
    )
