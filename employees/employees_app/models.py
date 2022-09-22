from pyexpat import model
from re import RegexFlag
import re
from statistics import mode
from wsgiref.validate import validator
from django.db import models

from django.core.exceptions import ValidationError


class Posts(models.Model): # Модель с должностями
    post_id    = models.IntegerField(primary_key=True, serialize=True, editable=False)
    post_descr = models.CharField(unique=True, max_length=128, db_index=True, default='new')

    def __str__(self):
        return self.post_descr

class Users(models.Model):
    usr_id  = models.IntegerField(primary_key=True, serialize=True, editable=False)
    usr_fio = models.CharField(max_length=128, blank=False)
    usr_sex = models.CharField(max_length=1, choices=[('m', 'male'), ('f', 'female')])
    usr_post = models.ForeignKey('Posts', on_delete=models.SET_NULL ,null=True)
    
    def __str__(self):
        return self.usr_fio

class Contacts(models.Model):
    contact_id = models.IntegerField(primary_key=True, serialize=True, editable=False)
    usr_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    usr_contact = models.CharField(unique=True, max_length=128, blank=False, null=False)
    def __str__(self):
        return str(self.usr_id)

class Departments(models.Model):
    def validate_dep_code(value):
        reg = re.compile('^[A-Z]-[0-9]{2}-[0-9]{2}-[0-9]{2}$')
        if not reg.match(value) :
            raise ValidationError('Use format: F-00-00-00')

    dep_id = models.IntegerField(primary_key=True, serialize=True, editable=False)
    dep_code = models.CharField(max_length=128, unique=True, blank=False, validators=[validate_dep_code])
    dep_description = models.CharField(max_length=256)
    dep_status = models.CharField(max_length=128, blank=False, choices=[('active', 'active'),('inactive', 'inactive')], default='active')

    def __str__(self):
        return self.dep_code + " " + self.dep_description
    # dep_mother_dep = models.ForeignKey('Departments', on_delete=models.SET_NULL, blank=True, null=True, related_name='dep_id')

class Usr_Dep(models.Model):
    usr_id = models.OneToOneField(Users, on_delete=models.CASCADE)
    dep_id = models.ForeignKey(Departments, on_delete=models.CASCADE)
    date_of_transition = models.DateField(null=False, editable=True)

    def __str__(self):
        return str(self.usr_id)

class Emp_Chef(models.Model):
    usr_id = models.OneToOneField(Users, primary_key=True, on_delete=models.CASCADE, related_name="Emp_id")
    chef_id = models.ForeignKey(Users, on_delete=models.PROTECT,  related_name="Chef_name")

    def __str__(self):
        return str(self.usr_id)

class Dep_Director(models.Model):
    dir_id = models.ForeignKey(Users, on_delete=models.PROTECT)
    dep_id = models.OneToOneField(Departments, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.dep_id)