# Generated by Django 4.2.5 on 2023-10-11 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='lol',
        ),
    ]
