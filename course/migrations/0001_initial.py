# Generated by Django 2.1.5 on 2020-08-13 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_curse', models.CharField(max_length=20)),
                ('capacity_curse', models.SlugField()),
                ('credits', models.IntegerField()),
            ],
        ),
    ]
