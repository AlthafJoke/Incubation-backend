from django.db import models
from django.contrib.auth.models import  AbstractBaseUser,PermissionsMixin
from .manager import UserManager


class User(AbstractBaseUser,PermissionsMixin):
    email               = models.EmailField(max_length=100,unique=True)
    phone_no            = models.CharField(max_length=12,null=False,blank=False)
    first_name          = models.CharField(max_length=50)
    last_name           = models.CharField(max_length=50)
    Company           = models.CharField(max_length=200,null=True,blank=True)
    
    is_admin            = models.BooleanField(default=False)
    is_staff            = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=True)
    is_superadmin       = models.BooleanField(default=False)
    created_date        =   models.DateTimeField(auto_now_add=True)
    modified_date       =   models.DateTimeField(auto_now=True)
    record_status       =   models.CharField(max_length=255,default='created')
    objects =UserManager()
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS =['phone_no','first_name', 'last_name']
    
    def _str_(self) :
        return self.email
    
    def has_perm(self,prem,obj=None):
        return True
    
    def has_module_perms(self,app_lable):
        return True
    
    def fullname(self):
        return "{} {}".format(self.first_name,self.last_name)

