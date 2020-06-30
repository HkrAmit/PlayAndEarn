from django.urls import path
from . import views

urlpatterns = [
    path('matches/', views.matches, name="matches"),
    path('matche/<int:match_id>/', views.reg_for_match, name="reg-for-match"),
]
