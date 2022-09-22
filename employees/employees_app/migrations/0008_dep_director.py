# Generated by Django 4.1.1 on 2022-09-18 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees_app', '0007_alter_usr_dep_usr_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dep_Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employees_app.departments')),
                ('dir_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employees_app.users')),
            ],
        ),
    ]
