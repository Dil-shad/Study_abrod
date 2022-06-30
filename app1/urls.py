from django.urls import path
from . import views 
from django.contrib import admin
from django.contrib.auth import views as auth_views
urlpatterns = [
        path('',views.dashboard, name='dashboard' ),
        path('team_leader_clints',views.team_leader_clints,name='team_leader_clints'),
        path('previous_leads',views.previous_leads,name='previous_leads'),
        path('sales_executive',views.sales_executive,name='sales_executive'),
        path('executive_dashboards',views.executive_dashboards,name='executive_dashboards'),
        path('exe_previous_leads',views.exe_previous_leads,name='exe_previous_leads'),
        path('current_leads',views.current_leads,name='current_leads'),
        path('newly_assigned_leads',views.newly_assigned_leads,name='newly_assigned_leads'),
        path('status_progress',views.status_progress,name='status_progress'),

]