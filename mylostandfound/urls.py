from udus_lost_and_found import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('custom-admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('', include('udus_lost_and_found.urls')),

]
