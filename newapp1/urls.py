from django.urls import path
from . import views

urlpatterns = [
    path('register-client/', views.register_client, name='register_client'),
    path('client/<int:client_id>/', views.client_info, name='client_info'),
    path('client/<int:client_id>/edit/', views.edit_client, name='edit_client'),
    path('client/<int:client_id>/delete/', views.delete_client, name='delete_client'),
    path('client/<int:client_id>/add-project/', views.add_project, name='add_project'),
    path('assigned-projects/', views.assigned_projects, name='assigned_projects'),
]
