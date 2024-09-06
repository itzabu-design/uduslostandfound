from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'templates/home'),
    path('', views.sign_up, name='templates/sign_up'),  
    path('report/', views.found_report, name='templates/found_report'),
    path('report/', views.lost_report, name='templates/lost_report'),
    path('', views.view_items, name='templates/view_items'),
    path('', views.help_page, name='help_page'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/manage_users/', views.manage_users, name='manage_users'),
    path('admin/system_settings/', views.system_settings, name='system_settings'),
    path('admin/manage_lost_items/', views.manage_lost_items, name='manage_lost_items'),
    path('admin/manage_found_items/', views.manage_found_items, name='manage_found_items'),
    path('admin/notifications/', views.notifications, name='notifications'),
    path('admin/reports/', views.reports, name='reports'),
]