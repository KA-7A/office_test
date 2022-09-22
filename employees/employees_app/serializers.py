from asyncore import read
from dataclasses import fields
from email.policy import default
from rest_framework import serializers
from .models import *
import datetime

class Posts_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = "__all__"

class Users_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"

class Contacts_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = "__all__"
class Departments_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = "__all__"

class Usr_Dep_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Usr_Dep
        fields = "__all__"
   
class Emp_Chef_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Emp_Chef
        fields = "__all__"

class Dep_Director_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Dep_Director
        fields = "__all__"