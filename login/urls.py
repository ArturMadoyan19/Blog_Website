from django.urls import path
from . import views

urlpatterns =[
    path('', views.login_ui, name="login"),
    path('check',views.check_login, name="check"),
]