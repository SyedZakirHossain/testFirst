
from django.db import models

class Taxpayer(models.Model):
    name = models.CharField(max_length=255,null=True)
    nid = models.IntegerField(null=True)
    
    def __str__ (self):
            return self.name
        
class Citizen(models.Model):
    name = models.CharField(max_length=255,null=True)
    nid = models.IntegerField(null=True)
    
    def __str__ (self):
            return self.name
        

class Bank(models.Model):
    bname = models.CharField(max_length=255,null=True)
    nid = models.IntegerField(null=True)
    #nid = models.ForeignKey(Citizen,null=True,on_delete=models.CASCADE)
    acno = models.IntegerField(null=True)
    balance = models.IntegerField(null=True)
    cname = models.ForeignKey(Citizen,null=True,on_delete=models.CASCADE)
    def __str__ (self):
            return self.bname





  
    

  