from django.urls import path
from . import views

urlpatterns = [
    path('requests/<int:pk>/update_status/', views.update_request_status, name='update_request_status'),
]