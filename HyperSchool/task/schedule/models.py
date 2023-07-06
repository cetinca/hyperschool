from django.db import models


# Create your models here.

# t1 = Teacher.objects.create(name="Albert", surname="Einstein", age="41", about="Experienced teacher")
# t2 = Teacher.objects.create(name="Isaac", surname="Newton", age="38", about="Experienced teacher")
# c1 = Course.objects.create(title="Python", info="Python 3.10", duration_months=12, price=120)
# c1.teacher.add(t1, t2)
# c1.teacher.all()


class Teacher(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    surname = models.CharField(max_length=100, blank=False, null=False)
    age = models.IntegerField()
    about = models.TextField(default="")


class Course(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    info = models.TextField(default="")
    duration_months = models.IntegerField()
    price = models.FloatField()
    teacher = models.ManyToManyField(Teacher)


class Student(models.Model):
    name = models.CharField(max_length=99, blank=False, null=False)
    surname = models.CharField(max_length=99, blank=False, null=False)
    age = models.IntegerField()
    course = models.ManyToManyField(Course)
