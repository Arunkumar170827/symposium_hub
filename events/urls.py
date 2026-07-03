from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/new/', views.create_registration, name='create_registration'),
    path('register/edit/<int:pk>/', views.update_registration, name='update_registration'),
    path('register/delete/<int:pk>/', views.delete_registration, name='delete_registration'),
]