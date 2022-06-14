from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name = 'index'),
    path('register', views.register, name = 'register'),
    path('login', views.login, name = 'login'),
    path('like/<image_id>', views.like, name='like'),
    path('show',views.show,name='show'),
    path('search',views.search,name='search'),
    path('comment/<image_id>',views.comment, name = 'comment'),
    path('follow/<user_id>', views.follow, name='follow'),
    path('like/<image_id>', views.like, name='like'),
]