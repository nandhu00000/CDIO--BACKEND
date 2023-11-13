
from django import db
from django.db import models

#Create your models here.
 
class summa(models.Model):
    
    name=models.CharField(null=True)
    descrip=models.CharField(null=True)


    

    class Meta:
        db.table="summa"
             
