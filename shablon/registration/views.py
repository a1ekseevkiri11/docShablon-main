from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.views import LoginView
from .forms import (
    StudentRegistrationForm,
    SupervisorOPOPRegistrationForm,
    SupervisorPracticeRegistrationForm,
)

from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
)

from . import permission



class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        if permission.isStudent(self.request.user):
            return reverse_lazy('student-practice-list')
        
        if permission.isSupervisorOPOP(self.request.user):
            return reverse_lazy('practice-list')
        
        if permission.isSupervisorPractice(self.request.user):
            return reverse_lazy('supervisor-practice-practice-student-list')
        

        return reverse_lazy('yes')


        
class Sucsess(LoginRequiredMixin, View):
    template_name = 'registration/yes.html'

    def get(self, request):
        return render(request, self.template_name)

        


class StudentRegistrationView(View):


    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


    def get(self, request):
        form = StudentRegistrationForm()
        group_name = "Студент"
        return render(request, self.template_name, {'form': form, 'group_name': group_name})
    

    def post(self, request):
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})
    


class SupervisorOPOPRegistrationView(View):


    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


    def get(self, request):
        form = SupervisorOPOPRegistrationForm()
        group_name = "Руководитель ОПОП"
        return render(request, self.template_name, {'form': form, 'group_name': group_name})
    

    def post(self, request):
        form = SupervisorOPOPRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})
    


class SupervisorPracticeRegistrationView(View):


    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


    def get(self, request):
        form = SupervisorPracticeRegistrationForm()
        group_name = "Руководитель Практики"
        return render(request, self.template_name, {'form': form, 'group_name': group_name})
    

    def post(self, request):
        form = SupervisorPracticeRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})
    
