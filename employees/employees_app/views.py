from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
import json

from .models import *
# Create your views here.

# Будем делать в формате одного адреса для всех действий с сотрудниками
# Управление будет осуществляться засчет разных кодов действий

"""
Что посылать:
{
    "type": type -> str,
    "request":
    {
        "arg1": arg1,
        "arg2": arg2, 
        ...
    }
}
Аргументы указаны в скобках после типа запроса
Как посылать: 
    \d.0.*      -- GET
    \d.1*       -- POST
    \d.2*       -- PUT
    \d.3*       -- DELETE
Доступные действия:

[Ахтунг! Всё, у чего args == '---' -- сейчас не работает, и я не планирую это исправлять в 
ближайшее время, потому что сейчас мне кажется это избыточным (но это не точно)]

1. Модель Posts -- 
type    args        comment
1.0                 Получить информацию обо всех должностях
1.1     post_descr  Добавить новую должность          
1.2     post,       Обновить название для должности
        post_decsr  
1.3     post        Удалить должность
1.3.1   ---         С установкой новой должности для всех сотрудников с этой должностью
1.3.2   ---         С установкой дефолтной должности для всех сотрудников с этой должностью

2. Модель Users --
2.0.0               Получить информацию обо всех пользовалеях (id, ФИО, пол, должность_id, должность_descr)
2.0.1   usr         Получить информацию о сотруднике 
2.1     usr_fio,    Добавить нового сотрудника
        usr_sex('m'/'f'),
        usr_post(post)
2.2     usr,        Обновить информацию
        usr_fio,
        usr_sex,
        usr_post
2.2.1   ---         Обновить ФИО         (полезно для отдела кадров, когда женщина выходит замуж, например)
2.2.2   ---         Обновить пол         (сами знаете, в какое время живём)
2.2.3   ---         Обновить должность   (понятно зачем)
2.3     usr         Удалить сотрудника (должна быть проверка, что человек не является руководителем ни одного из отделов)

3. Модель Contacts
3.0.0               Получить информацию обо всех контактах
3.0.1   usr         Получить информацию обо всех контактах одного пользователя   
3.1     usr,        Добавить новый контакт пользователю
        usr_contact 
3.2     contact,    Обновить контакт по номеру строки
        usr_contact 
3.3     contact     Удалить контакт

4. Модель Departments
4.0.0               Получить информацию обо всех отделах
4.0.1   dep         Получить информацию об одном отделе                           
4.1     dep_code,   Добавить новый отдел
        dep_descr,
        dep_status('active'/'inactive')
4.2     dep,        Обновить информацию об отделе
        dep_code,
        dep_descr,
        dep_status
4.2.1   ---         Обновить код подразделения
4.2.2   ---         Обновить описание подразделения
4.2.3   ---         Обновить руководителя
4.2.4   ---         Обновить статус подразделения (сделать проверку, что оно пустое)
4.3     dep         Удалить отдел

5. Модель Usr_Dep
5.0.0               Получить информацию обо всех департаментах
5.0.1   dep         Получить информацию об одном департаменте                     
5.0.2   usr         Получить информацию о департаменте одного сотрудника          
5.1     usr,
        dep         Добавить сотрудника в департамент
5.2     usr,
        dep         Перевести сотрудника из одного департамента в другой
5.3     usr         Исключить сотрудника из его департамента

6. Модель Emp_Chef 
6.0.0               Получить информацию обо всех начальниках
6.0.1   chef        Получить информацию обо всех подчиненных одного начальника    
6.0.2   usr         Получить информацию о начальнике одного сотрудника            
6.1     usr,
        chef        Добавить подчинённого (сделать проверку, что подчинённый не станет начальником своего начальника)
6.2     usr,
        chef        Сменить начальника:
6.2.1   ---         Сменить начальника одному пользователю
6.2.2   ---         Сменить начальника всем, у кого был этот начальник
6.3     usr         Удалить запись

7. Модель Dep_Director
7.0.0               Получить информацию обо всех директорах
7.0.1   dir         Получить информацию обо всех отделах одного директора        
7.0.2   dep         Получить информацию о директоре одного отдела                 
7.1     dep,
        dir         Добавить отделение
7.2     dep,
        dir         Сменить директора:
7.2.1   ---         Сменить директора одного отдела
7.2.2   ---         Сменить директора у всех отделов, где он был директором
7.3     dep         Удалить запись

"""
"""
Коды ошибок:
-1 -- неизвестный запрос
-2 -- некорректный запрос, не хватает поля
-3 -- указанная строка не найдена

"""

class EmployeesAPIView(APIView):
    def get(self, request):     
        # Здесь будет реализовано: [1-7].0.*
        if "type" not in request.data:
            return Response({"type": "-1", "description": "unknown request"})
        m_request = request.data
        match m_request["type"]:
            case "1.0.0":
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
                        "response": Users.objects.filter(usr_id = m_request["request"]["usr_id"]).values()
                    }))
                else:
                    return(Response({
                        "type": "-2",
                        "description": "usr is not specified"
                    }))
            
            case "3.0.0":
                return(Response({
                    "type": "3.0.0", 
                    "description": "get_all_user_contacts",
                    "response": Contacts.objects.all().values()}))
            case "3.0.1":
                if "usr_id" in m_request:
                    contacts_list = Contacts.objects.filter(usr = m_request["request"]['usr_id']).values()
                    return(Response({
                        "type": "3.0.1", 
                        "description": "get_one_user_contact",
                        "response": contacts_list}))
                else:
                    return(Response({
                        "type": "-2",
                        "description": "usr is not specified"}))
            
            case "4.0.0":
                return(Response({
                    "type": "4.0.0", 
                    "description": "get_all_departments_info",
                    "response": Departments.objects.all().values()}))
            case "4.0.1":
                if "dep_id" in m_request:
                    departments_list = Departments.objects.filter(dep = m_request["request"]['dep_id']).values()
                    return(Response({
                        "type": "3.0.1", 
                        "description": "get_one_departments_info",
                        "response": departments_list}))
                else:
                    return(Response({
                        "type": "-2",
                        "description": "dep is not specified"}))         
            
            case "5.0.0": 
                return(Response({
                    "type": "5.0.0", 
                    "description": "get_all_usr_dep_info",
                    "response": Usr_Dep.objects.all().values()}))
            case "5.0.1":
                if "dep_id" in m_request:
                    usr_dep_list = Usr_Dep.objects.filter(dep = m_request["request"]['dep_id']).values()
                    return (Response({
                        "type": "5.0.1", 
                        "description": "get_one_usr_dep_info",
                        "response": usr_dep_list}))
                else:
                    return(Response({
                        "type": "-2",
                        "description": "dep is not specified"}))
            case "5.0.2":
                if "usr_id" in m_request:
                    usr_dep = Usr_Dep.objects.filter(usr = m_request["request"]["usr"]).values()
                    return (Response({
                        "type": "5.0.2", 
                        "description": "get_one_usr_info",
                        "response": usr_dep}))
                else:
                    return(Response({
                        "type": "-2",
                        "description": "usr is not specified"}))
            
            case "6.0.0":
                return Response({
                    "type": "6.0.0",
                    "description": "get_all_chefs",
                    "response": Emp_Chef.objects.all().values()
                })
            case "6.0.1":
                if "chef_id" in m_request:
                    chef_list = Emp_Chef.objects.filter(chef = m_request["request"]["chef"]).values()
                    return (Response({
                        "type": "6.0.1", 
                        "description": "get_one_chef_info",
                        "response": chef_list}))
                else:
                    return(Response({
                        "type": "-2",
                        "description": "chef is not specified"}))
            case "6.0.2":
                if "usr_id" in m_request:
                    chef = Emp_Chef.objects.filter(usr = m_request["request"]["usr"]).values()
                    return (Response({
                        "type": "6.0.2", 
                        "description": "get_one_chef_info",
                        "response": chef}))
                else:
                    return(Response({
                        "type": "-2",
                        "description": "usr is not specified"}))
            
            case "7.0.0":
                return Response({
                    "type": "7.0.0",
                    "description": "get_all_dep_directors",
                    "response": Dep_Director.objects.all().values()
                })
            case "7.0.1":
                if "dir_id" in m_request:
                    deps_list = Dep_Director.objects.filter(dir = m_request["request"]["dir"]).values()
                    return (Response({
                        "type": "7.0.1", 
                        "description": "get_one_dir_info",
                        "response": deps_list}))
                else:
                    return(Response({
                        "type": "-2",
                        "description": "dir is not specified"}))
            case "7.0.2":
                if "dep_id" in m_request:
                    dep = Dep_Director.objects.filter(dep = m_request["request"]["dep_id"]).values()
                    return (Response({
                        "type": "7.0.2", 
                        "description": "get_one_dep_dir_info",
                        "response": dep}))
                else:
                    return(Response({
                        "type": "-2",
                        "description": "dep is not specified"}))

        return Response({"type": "-1", "description": "unknown request"})

    def post(self, request):   
        # Здесь будет реализовано: [1-7].1.*
        m_request = request.data
        if "type" not in m_request or "request" not in m_request:
            return Response({"type": "-2", "description": "type or request are not specified"})
        match m_request["type"]:
            case "1.1":
                serializer = Posts_Serializer(data=m_request["request"])
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response({"type": "1.1","response": serializer.data})
            case "2.1":
                serializer = Users_Serializer(data=m_request["request"])
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response({"type": "2.1","response": serializer.data})
            case "3.1":
                serializer = Contacts_Serializer(data=m_request["request"])
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response({"type": "3.1", "response": serializer.data})
            case "4.1":
                serializer = Departments_Serializer(data=m_request["request"])
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response({"type": "4.1", "response": serializer.data})
            case "5.1":
                serializer = Usr_Dep_Serializer(data = m_request["request"])
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response({"type": "5.1", "response": serializer.data})
            case "6.1":
                serializer = Emp_Chef_Serializer(data=m_request["request"])
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response({"type": "6.1", "response": serializer.data})
            case "7.1":
                serializer = Dep_Director_Serializer(data=m_request["request"])
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response({"type": "7.1", "response": serializer.data})
        return Response({"type": "-1", "description": "unknown request"})
    
    def put(self, request):     
        # Здесь будет реализовано: [1-7].2.*
        m_request = request.data
        if "type" not in m_request or "request" not in m_request:
            return Response({"type": "-2", "description": "type or request are not specified"})
        match m_request["type"]:
            case "1.2":
                if "post" not in m_request["request"]:
                    return Response({"type": "-2", "description": "post is not specified"}) 
                try:
                    instance = Posts.objects.get(post = m_request["request"]["post"])
                except:
                    return Response({"type": "-3", "description": "Such row does not exist"})
                serializer = Posts_Serializer(data = m_request["request"], instance=instance)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response({"type": "1.2", "response": serializer.data})
            case "2.2":
                if "usr" not in m_request["request"]:
                    return Response({"type": "-2", "description": "usr is not specified"})
                try:
                    instance = Users.objects.get(usr = m_request["request"]["usr"])
                except:
                    return Response({"type": "-3", "description": "Such row does not exist"})
                serializer = Users_Serializer(data = m_request["request"], instance=instance)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response({"type": "2.2", "response": serializer.data})

            case "3.2":
                if "contact" not in m_request["request"]:
                    return Response({"type": "-2", "description": "contact is not specified"})
                try:
                    instance = Contacts.objects.get(contact = m_request["request"]["contact"])
                except:
                    return Response({"type": "-3", "description": "Such row does not exist"})
                serializer = Contacts_Serializer(data = m_request["request"], instance=instance)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response({"type": "3.2", "response": serializer.data})

            case "4.2":
                if "dep" not in m_request["request"]:
                    return Response({"type": "-2", "description": "dep is not specified"})
                try:
                    instance = Departments.objects.get(dep = m_request["request"]["dep"])
                except:
                    return Response({"type": "-3", "description": "Such row does not exist"})
                serializer = Departments_Serializer(data = m_request["request"], instance=instance)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response({"type": "4.2", "response": serializer.data})

            case "5.2":
                if "usr" not in m_request["request"]:
                    return Response({"type": "-2", "description": "usr is not specified"})
                try:
                    instance = Usr_Dep.objects.get(usr = m_request["request"]["usr"])
                except:
                    return Response({"type": "-3", "description": "Such row does not exist"})
                serializer = Usr_Dep_Serializer(data = m_request["request"], instance=instance)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response({"type": "5.2", "response": serializer.data})
            
            case "6.2":
                if "chef" not in m_request["request"] and "usr" not in m_request["request"]:
                    return Response({"type": "-2", "description": "chef or usr is not specified"})
                try:
                    instance = Emp_Chef.objects.get(usr = m_request["request"]["usr"])
                except:
                    return Response({"type": "-3", "description": "Such row does not exist"})
                serializer = Emp_Chef_Serializer(data = m_request["request"], instance=instance)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response({"type": "6.2", "response": serializer.data})

            case "7.2":
                if "dir" not in m_request["request"] and "dep" not in m_request["request"]:
                    return Response({"type": "-2", "description": "dir or dep is not specified"})
                try:
                    instance = Dep_Director.objects.get(usr = m_request["request"]["usr"])
                except:
                    return Response({"type": "-3", "description": "Such row does not exist"})
                serializer = Dep_Director_Serializer(data = m_request["request"], instance=instance)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response({"type": "7.2", "response": serializer.data})

        return Response({"type": "-1", "description": "unknown request"})

    def delete(self, request):  
        # Здесь будет реализовано: [1-7].3.*
        return Response({"type": "-1", "description": "unknown request"})



