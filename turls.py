from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [

    # Auth
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Profile
    path('profile/', views.ProfileView.as_view(), name='profile'),

    # Tasks
    path('tasks/', views.TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/status/', views.TaskStatusUpdateView.as_view(), name='task-status'),
    path('tasks/summary/', views.TaskSummaryView.as_view(), name='task-summary'),

    # Admin
    path('admin/users/', views.AdminUserListView.as_view(), name='admin-users'),
    path('admin/tasks/', views.AdminTaskListView.as_view(), name='admin-tasks'),
]
