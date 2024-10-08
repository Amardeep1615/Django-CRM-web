from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record


class SignUpForm(UserCreationForm):
    email= forms.EmailField(label ="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name= forms.CharField(label ="",max_length="100",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name= forms.CharField(label ="",max_length="100",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'password1','password2' )

def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customizing fields dynamically
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']= 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required.150 characters or fewer.Letters, digits and @/./+/-/_only.</small></span>'
        
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['placeholder']= 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be similar too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li></ul>'
        
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['placeholder']= 'Confirm Password'
        self.fields['password1'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before,for verfication.</small></span>'
        

    



    #Create Add Record Form
class AddRecordForm(forms.ModelForm):
     first_name = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"First_Name","class":"form-control"}),label="")
     last_name =  forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Last_Name","class":"form-control"}),label="")
     email =  forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Email","class":"form-control"}),label="")
     phone =  forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Phone","class":"form-control"}),label="")
     address =  forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Address","class":"form-control"}),label="")
     city =  forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"City","class":"form-control"}),label="")
     state =  forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"State","class":"form-control"}),label="")
     zipcode =  forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode","class":"form-control"}),label="")
    
     class Meta:
          model = Record
          exclude = ("user",)

