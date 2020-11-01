from django.urls import path

from blog import views

urlpatterns = [
    path('posts/', views.post_list, name='home'),
    path('posts/<str:category_name>', views.post_list, name='post_list'),
    path('posts/detail/<int:post_id>', views.post_detail, name='post_detail'),
]
