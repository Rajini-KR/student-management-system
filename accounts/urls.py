from django.urls import path
from .views import (
    CustomLoginView,
    CustomLogoutView,  # <-- Must match the class name in views.py exactly
    ProfileView,
    RegisterView,
)

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
]