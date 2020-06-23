from django.http import HttpResponse
from django.template import loader

from .models import Teacher


def index(request):
    index_template = loader.get_template("index.html")
    teachers = Teacher.objects.all()

    return HttpResponse(index_template.render({"teachers": teachers}, request))
