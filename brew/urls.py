from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib import admin

from . import views


app_name = 'brew'
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('brew/', views.new_brew, name='new_brew'),
    path('roast/', views.new_roast, name='new_roast'),
    path('register', views.register, name='register'),
    path('brew/<int:brew_id>/', views.brew_profile, name='brew_profile'),
    path('brew/<int:brew_id>/update/', views.update_brew, name='update_brew'),
    path('brew/<int:brew_id>/delete/', views.brew_delete, name='brew_delete'),
    path('roast/<int:roast_id>/', views.roast_profile, name='roast_profile'),
    path('roast/<int:roast_id>/update', views.update_roast, name='update_roast'),
    path('roast/<int:roast_id>/delete', views.roast_delete, name='roast_delete'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),



]