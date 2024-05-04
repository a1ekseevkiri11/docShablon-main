from django.urls import path
from . import views


urlpatterns = [
    path('practices/', views.PracticeListView.as_view(), name='student-practice-list'),
    path('practice/<int:pk>/', views.PracticeDetailView.as_view(), name='student-practice-detail'),
    path('practiceStudent/<int:practice_id>/parseFile/', views.StudentProductionTasksCreateView.as_view(), name='student-practice-student-parse-file'),
]