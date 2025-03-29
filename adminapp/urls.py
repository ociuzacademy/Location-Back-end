from django.urls import path
from . import views

from .views import *
urlpatterns = [
    path('admin_index/', views.admin_index, name='admin_index'), 
    path('',views.admin_login,name='admin_login'),
    path('admin_logout/',views.admin_logout,name='admin_logout'),
    path('add_category/', views.add_category, name='add_category'),
    path('categories/', views.list_categories, name='list_categories'),
    path('categories/edit/<int:category_id>/', views.edit_category, name='edit_category'),
    path('categories/delete/<int:category_id>/', views.delete_category, name='delete_category'),
     path("add_ward/", views.add_ward, name="add_ward"),
     path("wards/", views.list_wards, name="list_wards"),
     path("edit-ward/<int:ward_id>/", views.edit_ward, name="edit_ward"),
     path('ward/delete/<int:ward_id>/', views.delete_ward, name='delete_ward'),
   path("requests/", views.ward_requests, name="ward_requests"),
    path("requests/<int:ward_id>/", views.ward_request_details, name="ward_request_details"),
     path("register/", views.register_employee, name="register_employee"),
      path("employees/", list_employees, name="list_employees"),
    path("employees/edit/<int:employee_id>/", edit_employee, name="edit_employee"),
    path("employees/delete/<int:employee_id>/", delete_employee, name="delete_employee"),
    path('feedbacks/', admin_feedback_list, name='admin_feedback_list'),
    















    path('view-drivers/', views.admin_view_driver, name='admin_view_driver'),
    path('approve-driver/<int:driver_id>/', approve_driver, name='approve_driver'),
    path('reject-driver/<int:driver_id>/', reject_driver, name='reject_driver'),
     path('view-approved-drivers/', view_approved_drivers, name='view_approved_drivers'),
    path('view-rejected-drivers/', view_rejected_drivers, name='view_rejected_drivers'),
    path('view-complaints/', view_complaints, name='view_complaints'),
     path('allocate-complaint/<int:complaint_id>/', allocate_complaint, name='allocate_complaint'),
    path('assign-driver/<int:complaint_id>/<int:driver_id>/', assign_driver, name='assign_driver'),
     path('update-bin-status/<int:complaint_id>/<str:status>/', update_bin_status, name='update_bin_status'),

    
]
