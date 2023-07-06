from django.urls import path
from schedule import views

app_name = "schedule"

urlpatterns = [
    path('main/', views.main, name='main'),
    path('course_details/<int:cid>/', views.course_details, name='course_details'),
    path('teacher_details/<int:cid>/', views.teacher_details, name='teacher_details'),
    path('add_course/', views.add_course, name='add_course'),
]
