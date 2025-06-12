from django.urls import path
from . import views

urlpatterns = [
    path('', views.flight_list, name='flight_list'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
