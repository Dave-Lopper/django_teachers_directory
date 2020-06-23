from django.urls import path

from . import views

app_name = 'directory'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('subject/<int:subject_id>/', views.subject, name='subject'),
    path('teacher/<int:teacher_id>/', views.teacher, name='teacher'),
    path('', views.index, name='index'),
]
