from django.urls import path
from authapp import views

app_name = "authsapp"

urlpatterns = [
    path('registration/', views.Registration.as_view(), name="registration"),
    path('login/', views.Login.as_view(), name="login"),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.Profile.as_view(), name='profile')
]
