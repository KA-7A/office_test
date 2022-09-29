"""employees URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employees_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/employees',                           EmployeesAPIView.as_view()),
    path('api/v1/employees/<int:usr_id>',              EmployeesAPIView.as_view()),
    path('api/v1/employees/<int:usr_id>/<int:dep_id>', EmployeesAPIView.as_view()),

    path('api/v1/position',                             PositionAPIView.as_view()),
    path('api/v1/position/<int:position_id>',           PositionAPIView.as_view()),

    path('api/v1/users',                                UsersAPIView.as_view()),
    path('api/v1/users/<int:user_id>',                  UsersAPIView.as_view()),

    path('api/v1/contacts',                                 ContactsAPIView.as_view()),
    path('api/v1/contacts/<int:user_id>',                   ContactsAPIView.as_view()),
    path('api/v1/contacts/<int:user_id>/<int:contact_id>',  ContactsAPIView.as_view()),

    path('api/v1/departments',                          DepartmentsAPIView.as_view()),
    path('api/v1/departments/<int:dep_id>',             DepartmentsAPIView.as_view()),

    path('api/v1/chef',                                 ChefAPIView.as_view()),
    path('api/v1/chef/<int:user_id>',                   ChefAPIView.as_view()),
    path('api/v1/chef/<int:user_id>/<int:chef_id>',     ChefAPIView.as_view()),

    path('api/v1/director',                             DirectorAPIView.as_view()),
    path('api/v1/director/<int:user_id>',               DirectorAPIView.as_view()),
    path('api/v1/director/<int:user_id>/<int:dep_id>',  DirectorAPIView.as_view()),
]
