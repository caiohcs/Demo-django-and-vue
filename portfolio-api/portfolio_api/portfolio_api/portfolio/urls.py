from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('portfolio/', views.TechnologyList.as_view()),
    path('portfolio/<int:pk>/', views.TechnologyDetail.as_view()),
]