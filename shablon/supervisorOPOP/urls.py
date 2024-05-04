from django.urls import path
from . import views


urlpatterns = [
    path('practices/', views.PracticesListView.as_view(), name='practice-list'),
    path('practice/<int:pk>/', views.PracticesDetailView.as_view(), name='practice-detail'),
    path('practice/new/', views.PracticeCreateView.as_view(), name='practice-new'),
    path('practice/update/<int:pk>/', views.PracticeUpdateView.as_view(), name='practice-update'),
    path('practice/delete/<int:pk>/', views.PracticeDeleteView.as_view(), name='practice-delete'),
    path('group', views.get_groups, name='get-groups'),
    path('directionOfTraining/<int:pk>/', views.DirectionOfTrainingDetailView.as_view(), name='direction_of_training_detail'),
    path('reportGroup/', views.ReportGroupListView.as_view(), name='ready-report-group-list'),
    path('reportGroup/<int:pk>/', views.ReportGroupDetailView.as_view(), name='ready-report-group-detail'),
]