from django.urls import path
from . import views

urlpatterns = [
    path('', views.ui, name='post_ui'),
    path('add/', views.add_post,name="add_post"),
    path('get/', views.get_posts),
    path('delete/<int:post_id>/',views.delete_posts,name='delete_post'),
    path('logout/', views.logout, name='logout'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post')
]
