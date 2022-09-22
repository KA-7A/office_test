from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Users)
admin.site.register(Contacts)
admin.site.register(Posts)
admin.site.register(Departments)
admin.site.register(Usr_Dep)
admin.site.register(Dep_Director)
admin.site.register(Emp_Chef)