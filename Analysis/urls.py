from django.contrib import admin
from django.urls import path
from Analysis import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('setup/', views.setup_view, name='setup'),
]