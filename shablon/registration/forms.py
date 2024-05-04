from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from user.models import (
    Student,
    Group,
    SupervisorPractice,
    SupervisorOPOP,
)

from django.forms import Select

class ProfileRegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True, help_text='Имя')
    last_name = forms.CharField(required=True, help_text='Фамилия')
    patronymic = forms.CharField(required=True, help_text='Отчество')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Вызов метода __init__ родительского класса
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class StudentRegistrationForm(ProfileRegistrationForm):

    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True, widget=Select(attrs={'class': 'form-select form-select-lg mb-3'}))

    class Meta(ProfileRegistrationForm.Meta):
        model = User
        fields = ('username', 'last_name', 'first_name',  'patronymic', 'group', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        student = Student.objects.create(
            user=user, 
            group=self.cleaned_data['group'],
            first_name = self.cleaned_data['first_name'],
            last_name = self.cleaned_data['last_name'],
            patronymic = self.cleaned_data['patronymic'],
            )
        return user
    

class AbstractSupervisorRegistrationForm(ProfileRegistrationForm):

    post = forms.CharField(required=True, help_text='Пост')

    class Meta(ProfileRegistrationForm.Meta):
        abstract = True
        model = User
        fields = ('username', 'post', 'last_name', 'first_name',  'patronymic', 'password1', 'password2')
    

class SupervisorOPOPRegistrationForm(AbstractSupervisorRegistrationForm):


    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        supervisorOPOP = SupervisorOPOP.objects.create(
            user=user, 
            post=self.cleaned_data['post'],
            first_name = self.cleaned_data['first_name'],
            last_name = self.cleaned_data['last_name'],
            patronymic = self.cleaned_data['patronymic'],
            )
        return user



class SupervisorPracticeRegistrationForm(AbstractSupervisorRegistrationForm):


    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        supervisorPractice = SupervisorPractice.objects.create(
            user=user, 
            post=self.cleaned_data['post'],
            first_name = self.cleaned_data['first_name'],
            last_name = self.cleaned_data['last_name'],
            patronymic = self.cleaned_data['patronymic'],
            )
        return user