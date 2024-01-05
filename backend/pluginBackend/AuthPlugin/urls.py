from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login',views.login ),
    path('logout',views.logout),
    path('google/', views.GoogleLogin.as_view(), name='google_login')
]