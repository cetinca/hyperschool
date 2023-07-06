from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from schedule.models import Course, Student


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"


class SearchForm(forms.Form):
    q = forms.CharField(max_length=255)


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "surname", "age", "course"]


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
