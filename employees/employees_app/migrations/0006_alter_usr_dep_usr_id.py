# Generated by Django 4.1.1 on 2022-09-18 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees_app', '0005_alter_departments_dep_code_usr_dep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usr_dep',
            name='usr_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees_app.users', unique=True),
        ),
    ]
