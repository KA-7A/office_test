# Generated by Django 4.1.1 on 2022-09-22 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees_app', '0013_alter_departments_dep_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='id',
        ),
        migrations.RemoveField(
            model_name='emp_chef',
            name='id',
        ),
        migrations.AddField(
            model_name='contacts',
            name='contact_id',
            field=models.IntegerField(default=12, editable=False, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='emp_chef',
            name='usr_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='Emp_id', serialize=False, to='employees_app.users'),
        ),
    ]
