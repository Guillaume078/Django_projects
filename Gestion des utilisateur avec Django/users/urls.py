from users.views import dashboard, register
from django.urls import re_path, include, path
urlpatterns=[
    path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard/", dashboard, name="dashboard"),
    path("register/", register, name="register"),
    path("oauth/", include("social_django.urls")),
]
