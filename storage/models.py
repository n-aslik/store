

from django.db import models
from django.forms import ModelForm, Textarea
from django.contrib.auth.models import AbstractUser



class Userlogin(AbstractUser):
    fio=models.CharField(max_length=45,verbose_name="ФИО")
    pos=models.ForeignKey("Position",verbose_name="Должность",on_delete=models.CASCADE, null=True, blank=True)
    tel=models.IntegerField("Тел",null=True, blank=True)
    rol=models.ForeignKey("Role",verbose_name="Роль",on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.fio
        
    
    
class Role(models.Model):
    code=models.CharField("Код",max_length=45)
    rname=models.CharField("Наименование",max_length=45)

    def __str__(self):
        return self.rname
    
class Branch(models.Model):
    address=models.CharField("Адрес",max_length=50)
    bname=models.CharField("Наименование",max_length=45)
    user=models.ForeignKey("Userlogin",verbose_name="Пользователь",on_delete=models.CASCADE)
    
    def __str__(self):
        return self.bname
    
    
class Storage(models.Model):
    sname=models.CharField("Наименование",max_length=45)
    user=models.ForeignKey("Userlogin",verbose_name='Пользователь',on_delete=models.CASCADE)
    branch=models.ForeignKey("Branch",verbose_name="Филиал",on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.sname
        
    
    
    
class Incoming(models.Model):
    iname=models.CharField("Наименование",max_length=45)
    counti=models.IntegerField("количество")
    incoming_date=models.DateField("Дата прихода")
    recipient=models.CharField("получатель",max_length=50)
    store=models.ForeignKey("Storage",verbose_name="Склад",on_delete=models.CASCADE,null=True, blank=True)
    user=models.ForeignKey("Userlogin",verbose_name='Пользователь',on_delete=models.CASCADE)
    
    def __str__(self):
        if self.counti<=0:
            return ''
        else:
            return self.iname +':'+ str(self.counti)
    
class Outcoming(models.Model):
    inc=models.ForeignKey("Incoming",verbose_name="Приход",on_delete=models.CASCADE)
    counto=models.IntegerField("количество")
    recipient=models.CharField("получатель",max_length=50)
    store=models.ForeignKey("Storage",verbose_name="Склад",on_delete=models.CASCADE,null=True, blank=True)
    outcoming_date=models.DateField("Дата расхода")
    user=models.ForeignKey("Userlogin",verbose_name='Пользователь',on_delete=models.CASCADE)
    
class Branch_access(models.Model):
    branch=models.ForeignKey("Branch",verbose_name="Филиал",on_delete=models.CASCADE,null=True, blank=True)
    user=models.ForeignKey("Userlogin",verbose_name='Пользователь',on_delete=models.CASCADE)
    store=models.ForeignKey("Storage",verbose_name="Склад",on_delete=models.CASCADE, null=True, blank=True)

  
            
            
        
    
class Position(models.Model):
    pname=models.CharField("Наименование",max_length=50)

    def __str__(self):
        return self.pname

    

# Create your models here.

# Create your models here.
