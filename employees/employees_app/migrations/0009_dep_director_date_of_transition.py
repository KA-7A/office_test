# Generated by Django 4.1.1 on 2022-09-18 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees_app', '0008_dep_director'),
    ]

    operations = [
        migrations.AddField(
            model_name='dep_director',
            name='date_of_transition',
            field=models.DateField(auto_now=True),
        ),
    ]
