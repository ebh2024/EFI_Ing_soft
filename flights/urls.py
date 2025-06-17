from django.urls import path
from . import views

urlpatterns = [
    path('', views.flight_list, name='flight_list'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('flight/<int:flight_id>/seats/', views.seat_availability, name='seat_availability'),
    path('flight/<int:flight_id>/passengers/', views.passengers_by_flight, name='passengers_by_flight'),
    path('home/', views.home, name='home'),
]
