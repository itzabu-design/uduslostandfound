from django.urls import path
from . import views
from django.shortcuts import render
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.home, name='home'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('report-found/', views.found_report, name='found_report'),
    path('report-lost/', views.lost_report, name='lost_report'),
    path('items/', views.view_items, name='view_items'),
    path('help/', views.help_view, name='help_page'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/manage_users/', views.manage_users, name='manage_users'),
    path('admin/system_settings/', views.system_settings, name='system_settings'),
    path('admin/manage_lost_items/', views.manage_lost_items, name='manage_lost_items'),
    path('admin/manage_found_items/', views.manage_found_items, name='manage_found_items'),
    path('admin/notifications/', views.notifications, name='notifications'),
    path('admin/reports/', views.reports, name='reports'),
    path('profile/', views.profile, name='profile'),
     path('lost-report/', views.lost_report, name='lost_report'),
    path('found-report/', views.found_report, name='found_report'),
]