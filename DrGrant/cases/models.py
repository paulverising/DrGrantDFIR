from xmlrpc.client import DateTime
from django.db import models
from django.forms import CharField, DateTimeField
from django.contrib.auth.models import User
from django.urls import reverse

class Case(models.Model):
    name = models.CharField(max_length=200)
    dateCreated = models.DateTimeField(auto_now=False, auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True, auto_now_add=False)
    description = models.TextField()
    initialAccess = models.DateTimeField(editable=True, blank=True, null=True)
    firstDetectTime = models.DateTimeField(editable=True, blank=True, null=True)
    incidentManager = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cases-detail', kwargs={'pk': self.pk})

class System_Type(models.Model):
    type = models.CharField(max_length=200)
    dateCreated = models.DateTimeField(auto_now=False, auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.type

class System(models.Model):
    case = models.ForeignKey(Case, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    dateCreated = models.DateTimeField(auto_now=False, auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True, auto_now_add=False)
    description = models.TextField()
    is_Attacker = models.BooleanField()
    system_type = models.ForeignKey(System_Type, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name

class Account_Type(models.Model):
    type = models.CharField(max_length=200)
    dateCreated = models.DateTimeField(auto_now=False, auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.type
    
class Account(models.Model):
    case = models.ForeignKey(Case, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    dateCreated = models.DateTimeField(auto_now=False, auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True, auto_now_add=False)
    description = models.TextField()
    is_AttackerCreated = models.BooleanField()
    account_type = models.ForeignKey(Account_Type, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name
    

class Task_Status(models.Model):
    status = models.CharField(max_length=200)
    dateCreated = models.DateTimeField(auto_now=False, auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    class Meta:
        verbose_name_plural = "Task_statuses"
    
    def __str__(self):
        return self.status
    
class Task(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    dateCreated = models.DateTimeField(auto_now=False, auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True, auto_now_add=False)
    description = models.TextField()
    system = models.ForeignKey(System, blank=True, null=True, on_delete=models.PROTECT)
    task_status = models.ForeignKey(Task_Status, default=1, on_delete=models.PROTECT)
    assignee = models.ForeignKey(User, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


