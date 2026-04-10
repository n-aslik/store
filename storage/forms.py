
from django import forms
from storage.models import  Userlogin ,Incoming,Storage,Outcoming,Branch,Branch_access
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.utils import timezone




class userform(AuthenticationForm):
    pass

class userpageform(forms.ModelForm):
    class Meta:
        model=Userlogin
        fields=['fio','pos','tel','rol']
        
        
class incomingform(forms.ModelForm):
    class Meta:        
        model=Incoming
        fields=['user','iname','counti','recipient','incoming_date','store','unit', 'price', 'total_price']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Делаем поле необязательным, чтобы форма не ругалась на пустоту
        if 'total_price' in self.fields:
            self.fields['total_price'].required = False
            # Можно даже запретить его редактировать, так как считаем сами
            self.fields['total_price'].widget.attrs['readonly'] = True
        

class outcomingform(forms.ModelForm):
    class Meta:        
        model=Outcoming
        fields=['user','inc','counto','recipient','outcoming_date','store','unit', 'price', 'total_price']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Делаем поле необязательным, чтобы форма не ругалась на пустоту
        if 'total_price' in self.fields:
            self.fields['total_price'].required = False
            # Можно даже запретить его редактировать, так как считаем сами
            self.fields['total_price'].widget.attrs['readonly'] = True
        
        
class storeform(forms.ModelForm):
    class Meta:
        model=Storage
        fields=['sname','user','branch']

    
       
        
        
class branchform(forms.ModelForm):
    class Meta:        
        model=Branch
        fields=['address','bname','user']
        
        
class branch_accessform(forms.ModelForm):
    class Meta:        
        model=Branch_access
        fields=['user','branch','store']
        

class report_searchform(forms.Form):
    query_b=forms.CharField(label="Филиал", max_length=100)
    query_ds=forms.DateField(label="Начальная_Дата")
    query_de=forms.DateField(label="Конечная_Дата")

    

class loginform(userform):
    username=forms.CharField(label='Username')
    password=forms.CharField(label='Password',widget=forms.PasswordInput)
        
        
    
        
