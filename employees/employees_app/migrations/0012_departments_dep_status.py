# Generated by Django 4.1.1 on 2022-09-18 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees_app', '0011_alter_usr_dep_date_of_transition_emp_chef'),
    ]

    operations = [
        migrations.AddField(
            model_name='departments',
            name='dep_status',
            field=models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], default='inactive', max_length=128),
        ),
    ]