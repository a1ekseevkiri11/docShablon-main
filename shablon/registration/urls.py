from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as registration_views


urlpatterns = [
    path('register/student/', registration_views.StudentRegistrationView.as_view(), name='register-student'),
    path('register/supervisorOPOP/', registration_views.SupervisorOPOPRegistrationView.as_view(), name='register-supervisorOPOP'),
    path('register/supervisorPractice/', registration_views.SupervisorPracticeRegistrationView.as_view(), name='register-supervisorPractice'),
    path('yes/', registration_views.Sucsess.as_view(), name='yes'),
    path('login/', registration_views.CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]