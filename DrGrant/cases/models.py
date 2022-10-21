from xmlrpc.client import DateTime
from django.db import models
from django.forms import CharField, DateTimeField
from django.contrib.auth.models import User

class Cases(models.Model):
    name = models.CharField(max_length=200)
    dateCreated = models.DateTimeField(auto_now=False, auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True, auto_now_add=False)
    description = models.TextField()
    initialAccess = models.DateTimeField(editable=True)
    firstDetectTime = models.DateTimeField(editable=True)

class InScopeSystems(models.Model):
    case = models.ForeignKey(Cases, default=1, on_delete=models.SET_DEFAULT)
    name = models.CharField(max_length=200)
    dateCreated = models.DateTimeField(auto_now=False, auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True, auto_now_add=False)
    description = models.TextField()

class Tasks(models.Model):
    case = models.ForeignKey(Cases, default=1, on_delete=models.SET_DEFAULT)
    name = models.CharField(max_length=200)
    dateCreated = models.DateTimeField(auto_now=False, auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True, auto_now_add=False)
    description = models.TextField()
    system = models.ForeignKey(InScopeSystems, default=1, on_delete=models.SET_DEFAULT)

class Task_Status(models.Model):
    status = models.CharField(max_length=200)
    dateCreated = models.DateTimeField(auto_now=False, auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True, auto_now_add=False)


