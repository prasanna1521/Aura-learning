from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth_entry_view, name='auth_entry'),
    path('assessment/', views.assessment_view, name='assessment'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
]
