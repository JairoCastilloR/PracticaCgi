# Generated by Django 2.1.5 on 2020-08-13 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
            ],
        ),
    ]
