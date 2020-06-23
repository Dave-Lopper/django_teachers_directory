from django.shortcuts import get_object_or_404, render

from ..models import Subject, Teacher


def teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    return render(request, 'teacher.html', {'teacher': teacher})


def subject(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    return render(request, 'subject.html', {'subject': subject})
