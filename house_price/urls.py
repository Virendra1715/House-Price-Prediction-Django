from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='home'),

    path('predict/', views.predict, name='predict'),

    path('history/', views.history, name='history'),

    path('about/', views.about, name='about'),

    path('contact/', views.contact, name='contact'),

    path('register/',views.register, name='register'),

    path("login/", views.login_user, name="login"),

    path("logout/", views.logout_user, name="logout"),
]