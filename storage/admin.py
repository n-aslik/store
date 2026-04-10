from django.contrib import admin
from django.contrib import admin
from .models import Userlogin, Role,Branch,Storage,Incoming,Outcoming,Position,Branch_access, Unit
from django.contrib.auth.admin import UserAdmin
 
admin.site.register(Userlogin,UserAdmin)
admin.site.register(Role)
admin.site.register(Branch)
admin.site.register(Storage)
admin.site.register(Incoming)
admin.site.register(Outcoming)
admin.site.register(Branch_access)
admin.site.register(Position)
admin.site.register(Unit)

# Register your models here.
