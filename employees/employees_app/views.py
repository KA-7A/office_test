from tkinter.messagebox import NO
from urllib import request
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
import json

from .models import *


class PositionAPIView(APIView):
    def get(self, request, *args, **kwargs):    
        #URL
        position_id = kwargs.get("position_id", None)
        if position_id is None:
            return Response({"response": Positions.objects.all().values()})
        try:
            obj = Positions.objects.get(position=position_id)
        except Exception as err:
            return Response({"error": str(err)})
        return Response({"response": Positions_Serializer(obj).data})
    
    def post(self, request):
        # {
        #     "description" : str
        # }
        serializer = Positions_Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"response": serializer.data})

    def put(self, request, *args, **kwargs):
        # URL + 
        # {
        #     "description" : str
        # }
        position_id = kwargs.get("position_id", None)
        if position_id is None:
            return Response({"error": "method PUT is no awailable"})
        try:
            instance = Positions.objects.get(position=position_id)
        except Exception as err:
            return Response({"error": str(err)})
        serializer = Positions_Serializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"response": serializer.data})

    def delete(self, request, *args, **kwargs):
        # URL
        position_id = kwargs.get("position_id", None)
        if position_id is None:
            return Response({"error": "method DELETE is no awailable"})
        try:
            obj = Positions.objects.get(position=position_id)
        except Exception as err:
            return Response({"error": str(err)})
        obj.delete()
        return Response({"response": "Ok"})

class UsersAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # URL
        user_id = kwargs.get("user_id", None)
        if user_id is None:
            return Response({"response": Users.objects.all().values()})
        try:
            obj = Users.objects.get(user=user_id)
        except Exception as err:
            return Response({"error": str(err)})
        return Response({"response": Users_Serializer(obj).data})
    
    def post(self, request):
        # Dict = {
        #     "usr_fio" : str,
        #     "usr_sex" : 'm'/'f',
        #     "usr_position_id": int
        # }
        serializer = Users_Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"response": serializer.data})

    def put(self, request, *args, **kwargs):
        # URL + Dict
        user_id = kwargs.get("user_id", None)
        if user_id is None:
            return Response({"error": "method PUT is no awailable"})
        try:
            instance = Users.objects.get(user=user_id)
        except Exception as err:
            return Response({"error": str(err)})
        serializer = Users_Serializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"response": serializer.data})

    def delete(self, request, *args, **kwargs):
        # URL
        user_id = kwargs.get("user_id", None)
        if user_id is None:
            return Response({"error": "method DELETE is no awailable"})
        try:
            obj = Users.objects.get(user=user_id)
        except Exception as err:
            return Response({"error": str(err)})
        obj.delete()
        return Response({"response": "Ok"})

class ContactsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # URL
        user_id = kwargs.get("user_id", None)
        if user_id is None:
            return Response({"response": Contacts.objects.all().values()})
        try:
            obj = Contacts.objects.get(usr=user_id)
        except Exception as err:
            return Response({"error": str(err)})
        return Response({"response": Contacts_Serializer(obj).data})
    
    def post(self, request):
        # Dict = {
        #     "usr": int,
        #     "usr_contact" : str
        # }
        serializer = Contacts_Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"response": serializer.data})
        

    def put(self, request, *args, **kwargs):
        # URL + Dict
        contact_id = kwargs.get("contact_id", None)
        if contact_id is None:
            return Response({"error": "method PUT is not awailable"})
        try:
            instance = Contacts.objects.get(contact=contact_id)
        except Exception as err:
            return Response({"error": str(err)})
        serializer = Contacts_Serializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"response": serializer.data})

    def delete(self, request, *args, **kwargs):
        # URL
        contact_id = kwargs.get("contact_id", None)
        if contact_id is None:
            return Response({"error": "method DELETE is not awailable"})
        try:
            obj = Contacts.objects.get(contact=contact_id)
        except Exception as err:
            return Response({"error": str(err)})
        obj.delete()
        return Response({"response": "Ok"})

class DepartmentsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # URL
        dep_id = kwargs.get("dep_id", None)
        if dep_id is None:
            return Response({"response": Departments.objects.all().values()})
        try:
            obj = Departments.objects.get(dep=dep_id)
        except Exception as err:
            return Response({"error": str(err)})
        return Response({"response": Departments_Serializer(obj).data})
    
    def post(self, request):
        # Dict = {
        #     "dep_code": str,
        #     "dep_description": str,
        #     "dep_status": str
        # }
        serializer = Departments_Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"response": serializer.data})
        

    def put(self, request, *args, **kwargs):
        # URL + Dict
        dep_id = kwargs.get("dep_id", None)
        if dep_id is None:
            return Response({"error": "method PUT is not awailable"})
        try:
            instance = Departments.objects.get(dep=dep_id)
        except Exception as err:
            return Response({"error": str(err)})
        serializer = Departments_Serializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"response": serializer.data})

    def delete(self, request, *args, **kwargs):
        # URL
        dep_id = kwargs.get("dep_id", None)
        if dep_id is None:
            return Response({"error": "method DELETE is not awailable"})
        try:
            obj = Departments.objects.get(dep=dep_id)
        except Exception as err:
            return Response({"error": str(err)})
        obj.delete()
        return Response({"response": "Ok"})

class EmployeesAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # URL
        usr_id = kwargs.get("usr_id", None)
        if usr_id is None:
            return Response({"response": Usr_Dep.objects.all().values()})
        try:
            obj = Usr_Dep.objects.get(usr=usr_id)
        except Exception as err:
            return Response({"error": str(err)})
        return Response({"response": Usr_Dep_Serializer(obj).data})
    
    def post(self, request, *args, **kwargs):
        # URL
        usr_id = kwargs.get("usr_id", None)
        dep_id = kwargs.get("dep_id", None)
        if usr_id is None or dep_id is None:
            return Response({"error" : "method POST is not awailable"})
        try:
            tmp_usr = Users.objects.get(user=usr_id)
            tmp_dep = Departments.objects.get(dep=dep_id)
        except Exception as err:
            return Response ({"error": str(err)})
        data = {"usr": usr_id, "dep": dep_id}
        serializer = Usr_Dep_Serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"response": serializer.data})
        

    def put(self, request, *args, **kwargs):
        # URL + {"date_of_transition" : "YYYY-MM-DD"}
        #TODO: Доделать изменение даты перевода
        usr_id = kwargs.get("usr_id", None)
        dep_id = kwargs.get("dep_id", None)
        if usr_id is None or dep_id is None:
            return Response({"error" : "method POST is not awailable"})
        if "date_of_transition" not in request.data:
            return Response({"error" : "date_of_transition is requiered"})
        try:
            tmp_usr = Users.objects.get(user=usr_id)
            tmp_dep = Departments.objects.get(dep=dep_id)
        except Exception as err:
            return Response ({"error": str(err)})
        data = {"usr": usr_id, "dep": dep_id, "date_of_transition": request.data["date_of_transition"]}
        try:
            instance = Usr_Dep.objects.get(usr=usr_id)
        except Exception as err:
            return Response({"error": str(err)})
        serializer = Usr_Dep_Serializer(data=data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"response": serializer.data})

    def delete(self, request, *args, **kwargs):
        # URL
        usr_id = kwargs.get("usr_id", None)
        if usr_id is None:
            return Response({"error": "method DELETE is not awailable"})
        try:
            obj = Usr_Dep.objects.get(usr=usr_id)
        except Exception as err:
            return Response({"error": str(err)})
        obj.delete()
        return Response({"response": "Ok"})

class ChefAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # URL
        usr_id = kwargs.get("user_id", None)
        if usr_id is None:
            return Response({"response": Emp_Chef.objects.all().values()})
        try:
            obj = Emp_Chef.objects.get(usr=usr_id)
        except Exception as err:
            return Response({"error": str(err)})
        return Response({"response": Emp_Chef_Serializer(obj).data})
    
    def post(self, request, *args, **kwargs):
        # URL
        usr_id = kwargs.get("user_id", None)
        chef_id = kwargs.get("dechef_idp_id", None)
        if usr_id is None or chef_id is None:
            return Response({"error" : "method POST is not awailable"})
        data = {"usr": usr_id, "chef": chef_id}
        serializer = Emp_Chef_Serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"response": serializer.data})
        

    def put(self, request, *args, **kwargs):
        # URL 
        usr_id = kwargs.get("user_id", None)
        chef_id = kwargs.get("chef_id", None)
        if usr_id is None or chef_id is None:
            return Response({"error" : "method PUT is not awailable"})
        data = {"usr": usr_id, "chef": chef_id}
        try:
            instance = Emp_Chef.objects.get(usr=usr_id)
        except Exception as err:
            return Response({"error": str(err)})
        serializer = Emp_Chef_Serializer(data=data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"response": serializer.data})

    def delete(self, request, *args, **kwargs):
        # URL
        usr_id = kwargs.get("usr_id", None)
        if usr_id is None:
            return Response({"error": "method DELETE is not awailable"})
        try:
            obj = Emp_Chef.objects.get(usr=usr_id)
        except Exception as err:
            return Response({"error": str(err)})
        obj.delete()
        return Response({"response": "Ok"})

class DirectorAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # URL
        usr_id = kwargs.get("user_id", None)
        if usr_id is None:
            return Response({"response": Dep_Director.objects.all().values()})
        try:
            obj = Dep_Director.objects.get(dir=usr_id)
        except Exception as err:
            return Response({"error": str(err)})
        return Response({"response": Dep_Director_Serializer(obj).data})
    
    def post(self, request, *args, **kwargs):
        # URL
        usr_id = kwargs.get("user_id", None)
        dep_id = kwargs.get("dep_id", None)
        if usr_id is None or dep_id is None:
            return Response({"error" : "method POST is not awailable"})
        data = {"dir": usr_id, "dep": dep_id}
        serializer = Dep_Director(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"response": serializer.data})
        

    def put(self, request, *args, **kwargs):
        # URL 
        usr_id = kwargs.get("user_id", None)
        dep_id = kwargs.get("dep_id", None)
        if usr_id is None or dep_id is None:
            return Response({"error" : "method PUT is not awailable"})
        data = {"dir": usr_id, "dep": dep_id}
        try:
            instance = Dep_Director.objects.get(dir=usr_id)
        except Exception as err:
            return Response({"error": str(err)})
        serializer = Dep_Director_Serializer(data=data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"response": serializer.data})

    def delete(self, request, *args, **kwargs):
        # URL
        usr_id = kwargs.get("usr_id", None)
        if usr_id is None:
            return Response({"error": "method DELETE is not awailable"})
        try:
            obj = Dep_Director.objects.get(dir=usr_id)
        except Exception as err:
            return Response({"error": str(err)})
        obj.delete()
        return Response({"response": "Ok"})

