from django.shortcuts import render, redirect, HttpResponse

from schedule.forms import StudentForm
from schedule.models import Course, Teacher, Student


# Create your views here.

def main(request):
    q = request.GET.get("q")
    if q:
        courses = Course.objects.filter(title__contains=q)
    else:
        courses = Course.objects.all()

    return render(request, 'schedule/main.html', {'courses': courses})


def course_details(request, cid):
    course = Course.objects.filter(id=cid).first()
    students = Student.objects.filter(course=course).all()
    t = course.teacher.all()
    return render(request, 'schedule/course_detail.html', {'course': course, 'students': students})


def teacher_details(request, cid):
    teacher = Teacher.objects.filter(id=cid).first()
    return render(request, 'schedule/teacher_detail.html', {'teacher': teacher})


def add_course(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database

            # Redirect to a success page or do something else
            return redirect('schedule:add_course')
    else:
        form = StudentForm

    return render(request, 'schedule/add_course.html', {'form': form})
