from django.urls import path
from . import views


urlpatterns = [
    path('practiceStudent/', views.PracticeStudentListView.as_view(), name='supervisor-practice-practice-student-list'),
    path('practiceStudent/<int:pk>/', views.PracticeStudentDetailView.as_view(), name='supervisor-practice-practice-student-detail'),
    path('practiceStudent/<int:practice_student_id>/rating/create/', views.RatingPracticeStudentCreateView.as_view(), name='rating-practice-practice-student-create'),
    path('practiceStudent/<int:practice_student_id>/rating/update/<int:pk>/', views.RatingPracticeStudentUpdateView.as_view(), name='rating-practice-practice-student-update'),
    path('reportGroup/', views.ReportGroupListView.as_view(), name='report-group-list'),
    path('report/<int:practice_id>/Group/<int:group_id>/create', views.ReportGroupCreateView.as_view(), name='report-group-create'),
]