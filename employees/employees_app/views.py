from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Usr_Dep_Serializer
import json

from .models import *
# Create your views here.

# Будем делать в формате одного адреса для всех действий с сотрудниками
# Управление будет осуществляться засчет разных кодов действий

"""
Доступные действия:
1. Модель Posts -- 
1.0   Получить информацию обо всех должностях
1.1   Добавить новую должность
1.2   Обновить название для должности
1.3   Удалить должность
1.3.1 С установкой новой должности для всех сотрудников с этой должностью
1.3.2 С установкой дефолтной должности для всех сотрудников с этой должностью

2. Модель Users --
2.0.0   Получить информацию обо всех пользовалеях (id, ФИО, пол, должность_id, должность_descr)
2.0.1   Получить информацию о сотруднике (usr_id)
2.1   Добавить нового сотрудника
2.2   Обновить информацию
2.2.1 Обновить ФИО         (полезно для отдела кадров, когда женщина выходит замуж, например)
2.2.2 Обновить пол         (сами знаете, в какое время живём)
2.2.3 Обновить должность   (понятно зачем)
2.3   Удалить сотрудника (должна быть проверка, что человек не является руководителем ни одного из отделов)

3. Модель Contacts
3.0.0 Получить информацию обо всех контактах
3.0.1 Получить информацию обо всех контактах одного пользователя    (usr_id)
3.1   Добавить новый контакт пользователю
3.2   Обновить контакт по номеру строки
3.3   Удалить контакт

4. Модель Departments
4.0.0 Получить информацию обо всех отделах
4.0.1 Получить информацию об одном отделе                           (dep_id)
4.1   Добавить новый отдел
4.2   Обновить информацию об отделе
4.2.1 Обновить код подразделения
4.2.2 Обновить описание подразделения
4.2.3 Обновить руководителя
4.2.4 Обновить статус подразделения (сделать проверку, что оно пустое)
4.3   Удалить отдел

5. Модель Usr_Dep
5.0.0 Получить информацию обо всех департаментах
5.0.1 Получить информацию об одном департаменте                     (dep_id)
5.0.2 Получить информацию о департаменте одного сотрудника          (usr_id)
5.1   Добавить сотрудника в департамент
5.2   Перевести сотрудника из одного департамента в другой
5.3   Исключить сотрудника из его департамента

6. Модель Emp_Chef 
6.0.0 Получить информацию обо всех начальниках
6.0.1 Получить информацию обо всех подчиненных одного начальника    (chef_id)
6.0.2 Получить информацию о начальнике одного сотрудника            (usr_id)
6.1   Добавить подчинённого (сделать проверку, что подчинённый не станет начальником своего начальника)
6.2   Сменить начальника:
6.2.1 Сменить начальника одному пользователю
6.2.2 Сменить начальника всем, у кого был этот начальник
6.3   Удалить запись

7. Модель Dep_Director
7.0.0 Получить информацию обо всех директорах
7.0.1 Получить информацию обо всех отделах одного директора         (dir_id)
7.0.2 Получить информацию о директоре одного отдела                 (dep_id)
7.1   Добавить отделение
7.2   Сменить директора:
7.2.1 Сменить директора одного отдела
7.2.2 Сменить директора у всех отделов, где он был директором
7.3   Удалить запись

"""
"""
Ошибки:
-1 -- неизвестный запрос
-2 -- некорректный запрос, не хватает поля

"""
"""
Мои замечания:
Почему-то, при запросе, у некоторых полей появляется дополнительная подстрока _id в конце. 
Это очень сильно напрягает, если честно

"""
class EmployeesAPIView(APIView):
    def get(self, request):     
        # Здесь будет реализовано: [1-7].0.*
        m_request = json.loads(request.body.decode('utf-8'))
        match m_request["type"]:
            case "1.0":
                return(Response({
                    "type": "1.0", 
                    "description":  "get_posts", 
                    "response": Posts.objects.all().values()}))
            
            case "2.0.0":
                return(Response({
                    "type": "2.0.0", 
                    "description": "get_all_users_info",
                    "response": Users.objects.all().values()}))
            case "2.0.1":
                if "usr_id" in m_request:
                    return(Response({
                        "type": "2.0.1",
                        "description": "get_one_user_info",
                        "response": Users.objects.filter(usr_id = m_request["usr_id"]).values()
                    }))
                else:
                    return(Response({
                        "type": "-2",
                        "description": "usr_id is not specified"
                    }))
            
            case "3.0.0":
                return(Response({
                    "type": "3.0.0", 
                    "description": "get_all_user_contacts",
                    "response": Contacts.objects.all().values()}))
            case "3.0.1":
                if "usr_id" in m_request:
                    contacts_list = Contacts.objects.filter(usr_id = m_request['usr_id']).values()
                    return(Response({
                        "type": "3.0.1", 
                        "description": "get_one_user_contact",
                        "response": contacts_list}))
                else:
                    return(Response({
                        "type": "-2",
                        "description": "usr_id is not specified"}))
            
            case "4.0.0":
                return(Response({
                    "type": "4.0.0", 
                    "description": "get_all_departments_info",
                    "response": Departments.objects.all().values()}))
            case "4.0.1":
                if "dep_id" in m_request:
                    departments_list = Departments.objects.filter(dep_id = m_request['dep_id']).values()
                    return(Response({
                        "type": "3.0.1", 
                        "description": "get_one_departments_info",
                        "response": departments_list}))
                else:
                    return(Response({
                        "type": "-2",
                        "description": "dep_id is not specified"}))         
            
            case "5.0.0": 
                return(Response({
                    "type": "5.0.0", 
                    "description": "get_all_usr_dep_info",
                    "response": Usr_Dep.objects.all().values()}))
            case "5.0.1":
                if "dep_id" in m_request:
                    usr_dep_list = Usr_Dep.objects.filter(dep_id = m_request['dep_id']).values()
                    return (Response({
                        "type": "5.0.1", 
                        "description": "get_one_usr_dep_info",
                        "response": usr_dep_list}))
                else:
                    return(Response({
                        "type": "-2",
                        "description": "dep_id is not specified"}))
            case "5.0.2":
                if "usr_id" in m_request:
                    usr_dep = Usr_Dep.objects.filter(usr_id = m_request["usr_id"]).values()
                    return (Response({
                        "type": "5.0.2", 
                        "description": "get_one_usr_info",
                        "response": usr_dep}))
                else:
                    return(Response({
                        "type": "-2",
                        "description": "usr_id is not specified"}))
            
            case "6.0.0":
                return Response({
                    "type": "6.0.0",
                    "description": "get_all_chefs",
                    "response": Emp_Chef.objects.all().values()
                })
            case "6.0.1":
                if "chef_id" in m_request:
                    chef_list = Emp_Chef.objects.filter(chef_id = m_request["chef_id"]).values()
                    return (Response({
                        "type": "6.0.1", 
                        "description": "get_one_chef_info",
                        "response": chef_list}))
                else:
                    return(Response({
                        "type": "-2",
                        "description": "chef_id is not specified"}))
            case "6.0.2":
                if "usr_id" in m_request:
                    chef = Emp_Chef.objects.filter(usr_id = m_request["usr_id"]).values()
                    return (Response({
                        "type": "6.0.2", 
                        "description": "get_one_chef_info",
                        "response": chef}))
                else:
                    return(Response({
                        "type": "-2",
                        "description": "usr_id is not specified"}))
            
            case "7.0.0":
                return Response({
                    "type": "7.0.0",
                    "description": "get_all_dep_directors",
                    "response": Dep_Director.objects.all().values()
                })
            case "7.0.1":
                if "dir_id" in m_request:
                    deps_list = Dep_Director.objects.filter(dir_id = m_request["dir_id"]).values()
                    return (Response({
                        "type": "7.0.1", 
                        "description": "get_one_dir_info",
                        "response": deps_list}))
                else:
                    return(Response({
                        "type": "-2",
                        "description": "dir_id is not specified"}))
            case "7.0.2":
                if "dep_id" in m_request:
                    dep = Dep_Director.objects.filter(dep_id = m_request["dep_id"]).values()
                    return (Response({
                        "type": "7.0.2", 
                        "description": "get_one_dep_dir_info",
                        "response": dep}))
                else:
                    return(Response({
                        "type": "-2",
                        "description": "dep_id is not specified"}))

        return Response({"type": "-1", "description": "unknown request"})

    def post(self, request):    # Добавление сотрудника в отдел
        # Здесь будет реализовано: [1-7].1.*
        return Response({'1': '2'})
    
    def put(self, request):     
        # Здесь будет реализовано: [1-7].2.*
        return Response({'3' : '4'})

    def delete(self, request):  
        # Здесь будет реализовано: [1-7].3.*
        return Response({'br': 'aaaa'})



