from django.contrib import admin
from .models import Case, System_Type, System, Task_Status, Task, Account_Type, Account

admin.site.register(Case)
admin.site.register(System_Type)
admin.site.register(System)
admin.site.register(Task_Status)
admin.site.register(Task)
admin.site.register(Account_Type)
admin.site.register(Account)


