from django.urls import path
from app_accounts_system import views

urlpatterns = [
    path('register/', views.register, name = "register")
]