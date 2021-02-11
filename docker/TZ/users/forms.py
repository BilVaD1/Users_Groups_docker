from .models import Users, Groups
from django.forms import ModelForm, TextInput, DateTimeInput


class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'created', 'group']

        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            'created': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Created date'
            })
        }


class GroupsForm(ModelForm):
    class Meta:
        model = Groups
        fields = ['Name', 'Description']

        widgets = {
            'Name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name of group'
            }),
            'Description': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Description of group'
            }),
        }
