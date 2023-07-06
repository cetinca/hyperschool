# Generated by Django 4.1.7 on 2023-03-06 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('info', models.TextField(default='')),
                ('duration_months', models.IntegerField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('about', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=99)),
                ('surname', models.CharField(max_length=99)),
                ('age', models.IntegerField()),
                ('course', models.ManyToManyField(to='schedule.course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ManyToManyField(to='schedule.teacher'),
        ),
    ]