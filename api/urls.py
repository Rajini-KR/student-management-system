from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    StudentListCreateAPI,
    StudentRetrieveUpdateDestroyAPI,
    DepartmentListAPI,
    CourseListAPI,
)

from .dashboard_views import DashboardAPIView
from .profile_views import ProfileAPIView
from .token_views import CustomTokenView


urlpatterns = [

    # -------------------------
    # JWT Authentication
    # -------------------------

    path(
        "token/",
        CustomTokenView.as_view(),
        name="token",
    ),

    path(
        "token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),

    # -------------------------
    # Dashboard
    # -------------------------

    path(
        "dashboard/",
        DashboardAPIView.as_view(),
        name="dashboard_api",
    ),

    # -------------------------
    # Profile
    # -------------------------

    path(
        "profile/",
        ProfileAPIView.as_view(),
        name="profile_api",
    ),

    # -------------------------
    # Students
    # -------------------------

    path(
        "students/",
        StudentListCreateAPI.as_view(),
        name="student-list",
    ),

    path(
        "students/<int:pk>/",
        StudentRetrieveUpdateDestroyAPI.as_view(),
        name="student-detail",
    ),

    # -------------------------
    # Departments
    # -------------------------

    path(
        "departments/",
        DepartmentListAPI.as_view(),
        name="department-list",
    ),

    # -------------------------
    # Courses
    # -------------------------

    path(
        "courses/",
        CourseListAPI.as_view(),
        name="course-list",
    ),

]