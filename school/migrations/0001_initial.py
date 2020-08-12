# Generated by Django 2.1.5 on 2020-08-12 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_number', models.IntegerField()),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_curse', models.CharField(max_length=20)),
                ('capacity_curse', models.SlugField()),
                ('credits', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_student', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('user_student', models.CharField(max_length=20)),
                ('date_creation_student', models.DateField(auto_now=True)),
                ('gender', models.BooleanField()),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Courses')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_teacher', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('dni', models.SlugField()),
                ('date_creation_teacher', models.DateField(auto_now=True)),
                ('gender', models.BooleanField()),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Courses')),
            ],
        ),
    ]
