from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('home/', views.home, name='home'),
    path('add_task/', views.add_task, name='add_task'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('update_data/',views.update_data,name='update_data'),
]