from django.urls import path

from . import views

app_name = 'directory'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('subject/<int:subject_id>/', views.subject, name='subject'),
    path('teacher/<int:teacher_id>/', views.teacher, name='teacher'),
    path('add-subject/', views.subject_add, name='subject_add'),
    path('add-teacher/', views.teacher_add, name='teacher_add'),
    path('import-teachers/', views.teacher_bulk_add, name='teacher_bulk_add'),
    path('', views.index, name='index'),
]
