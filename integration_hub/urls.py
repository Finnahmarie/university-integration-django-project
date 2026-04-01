from django.urls import path
from .views import student_summary

urlpatterns = [
    path('summary/<str:student_id>/', student_summary),
]