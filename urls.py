from django.urls import path
from . import user_views, admin_views

urlpatterns = [
    # User Endpoints
    path('register', user_views.register_user, name='register_user'),
    path('login', user_views.login_user, name='login_user'),
    path('upload', user_views.upload_assignment, name='upload_assignment'),

    # Admin Endpoints
    path('admin/register', admin_views.register_admin, name='register_admin'),
    path('admin/login', admin_views.login_admin, name='login_admin'),
    path('admin/assignments/<int:admin_id>', admin_views.view_assignments, name='view_assignments'),
    path('admin/assignments/<int:id>/accept', admin_views.accept_assignment, name='accept_assignment'),
    path('admin/assignments/<int:id>/reject', admin_views.reject_assignment, name='reject_assignment'),
]
