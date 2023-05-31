from django.urls import path
from studata import views

urlpatterns = [
    
        path('students/', views.StudentsList.as_view()),
        path('students/<int:pk>/', views.student_detail.as_view()),

]
