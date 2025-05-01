from django.urls import path
from . import views

urlpatterns =[
    path('', views.ui, name="ui"),
    path('reg',views.user_info, name="registration"),
    path('users/', views.get_user),
    path('delete/', views.clean_db),
]