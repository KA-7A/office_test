# Generated by Django 4.1.1 on 2022-09-18 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('post_id', models.IntegerField(default=1, editable=False, primary_key=True, serialize=False)),
                ('post_descr', models.CharField(db_index=True, default='new', max_length=128, unique=True)),
            ],
        ),
    ]
