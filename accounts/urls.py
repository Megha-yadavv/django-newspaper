from django.urls import path, include
from . import views

urlpatterns = [
    path('sign_up/', views.sign_up, name = 'signup' ),
    path('accounts/', include('django.contrib.auth.urls') ),#builtin log in , change password
    path('home/', views.home, name = 'home' )
]