from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('register/', views.register, name="register"),
    path('verify/<session>/', views.velidate_otp, name="verify"),
    path('verify/<session>/resend', views.resend_otp, name="resend"),
]