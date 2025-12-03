from django.urls import path
from . import views


urlpatterns = [
    # Public routes
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('support/', views.support, name='support'),
     path('report/', views.report_incident, name='report_incident'),
    path('thank-you/', views.thank_you, name='thank_you'),

    # Admin authentication routes

    path('login/', views.admin_login, name='admin_login'),
    path('logout/', views.admin_logout, name='admin_logout'),

    # Placeholder for dashboard
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # Admin incident management routes
    path('dashboard/incidents/', views.admin_incident_list, name='admin_incident_list'),
    path('dashboard/incidents/<int:incident_id>/', views.admin_incident_detail, name='admin_incident_detail'),
    path('dashboard/incidents/<int:incident_id>/edit/', views.admin_incident_edit, name='admin_incident_edit'),
    path('dashboard/incidents/<int:incident_id>/delete/', views.admin_incident_delete, name='admin_incident_delete'),
    path('dashboard/incidents/add/', views.admin_incident_add, name='admin_incident_add'),

    # Public dashboard route
    path('incidents/', views.public_incident_list, name='public_incident_list'),
    path('incidents/<int:incident_id>/', views.public_incident_detail, name='public_incident_detail'),





]
