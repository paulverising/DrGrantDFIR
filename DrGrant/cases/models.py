from xmlrpc.client import DateTime
from django.db import models
from django.forms import CharField, DateTimeField
from django.contrib.auth.models import User

class Case(models.Model):
    name = models.CharField(max_length=200)
    dateCreated = models.DateTimeField(auto_now=False, auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True, auto_now_add=False)
    description = models.TextField()
    initialAccess = models.DateTimeField(editable=True)
    firstDetectTime = models.DateTimeField(editable=True)

class System_Type(models.Model):
    type = models.CharField(max_length=200)
    dateCreated = models.DateTimeField(auto_now=False, auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True, auto_now_add=False)

class System(models.Model):
    case = models.ForeignKey(Case, default=1, on_delete=models.SET_DEFAULT)
    name = models.CharField(max_length=200)
    dateCreated = models.DateTimeField(auto_now=False, auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True, auto_now_add=False)
    description = models.TextField()
    is_Attacker = models.BooleanField()
    system_type = models.ForeignKey(System_Type, default=1, on_delete=models.SET_DEFAULT)

class Account_Type(models.Model):
    type = models.CharField(max_length=200)
    dateCreated = models.DateTimeField(auto_now=False, auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True, auto_now_add=False)
    
class Account(models.Model):
    case = models.ForeignKey(Case, default=1, on_delete=models.SET_DEFAULT)
    name = models.CharField(max_length=200)
    dateCreated = models.DateTimeField(auto_now=False, auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True, auto_now_add=False)
    description = models.TextField()
    is_AttackerCreated = models.BooleanField()
    account_type = models.ForeignKey(Account_Type, default=1, on_delete=models.SET_DEFAULT)
    

class Task_Status(models.Model):
    status = models.CharField(max_length=200)
    dateCreated = models.DateTimeField(auto_now=False, auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True, auto_now_add=False)
    
class Task(models.Model):
    case = models.ForeignKey(Case, default=1, on_delete=models.SET_DEFAULT)
    name = models.CharField(max_length=200)
    dateCreated = models.DateTimeField(auto_now=False, auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True, auto_now_add=False)
    description = models.TextField()
    system = models.ForeignKey(System, default=1, on_delete=models.SET_DEFAULT)
    task_status = models.ForeignKey(Task_Status, default=1, on_delete=models.SET_DEFAULT)
    assignee = models.ForeignKey(User, default="User Deleted", on_delete=models.SET_DEFAULT)



