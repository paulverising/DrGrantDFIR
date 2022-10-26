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
    incidentManager = models.ForeignKey(User, on_delete=models.PROTECT)
    
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

class Disposition_Type(models.Model):
    type = models.CharField(max_length=200)
    dateCreated = models.DateTimeField(auto_now=False, auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True, auto_now_add=False)

class System(models.Model):
    case = models.ForeignKey(Case, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    dateCreated = models.DateTimeField(auto_now=False, auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True, auto_now_add=False)
    description = models.TextField()
    is_Attacker = models.BooleanField()
    analysis_Required = models.BooleanField(default=None, null=True)
    disposition = models.ForeignKey(Disposition_Type, default=None, on_delete=models.PROTECT)
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
    remediated = models.BooleanField(default=None, null=True, blank=True)
    remediatedDate = models.DateTimeField(editable=True, blank=True, null=True)
    account_type = models.ForeignKey(Account_Type, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name
    

class NBI(models.Model):
    case = models.ForeignKey(Case, on_delete=models.PROTECT)
    ipAddress = models.GenericIPAddressField(blank=True, null=True)
    domain = models.URLField(blank=True, null=True)
    dateCreated = models.DateTimeField(auto_now=False, auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True, auto_now_add=False)
    description = models.TextField()
    remediated = models.BooleanField()
    remediatedDate = models.DateTimeField(editable=True, blank=True, null=True)
    
    def __str__(self):
        if self.ipAddress:
            return self.ipAddress
        elif self.domain:
            return self.domain
        else:
            return "NBI"
        
class HBI(models.Model):
    case = models.ForeignKey(Case, on_delete=models.PROTECT)
    fileName = models.CharField(max_length=300)
    filePath = models.CharField(max_length=300, blank=True, null=True)
    sha256 = models.CharField(max_length=64, blank=True, null=True)
    dateCreated = models.DateTimeField(auto_now=False, auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True, auto_now_add=False)
    description = models.TextField()
    sandboxLink = models.URLField()


    def __str__(self):
        return self.fileName

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


