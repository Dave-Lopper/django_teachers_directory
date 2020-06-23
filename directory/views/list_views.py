from django.shortcuts import render

from ..forms import TeacherFilterForm
from ..models import Teacher


def index(request):
    if request.method == 'POST':
        form = TeacherFilterForm(request.POST)
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

    form = TeacherFilterForm()
    teachers = Teacher.objects.all()
    return render(request, "index.html", {"teachers": teachers, "form": form})
