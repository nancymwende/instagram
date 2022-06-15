from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index,name = 'index'),
    path('signup', views.register, name = 'sign-up'),
    path('image',views.get_image_by_id,name ='image'),
    # path('login', views.login, name = 'login'),
    path('accounts/',include('registration.backends.simple.urls')),
    path('login/', auth_views.LoginView.as_view(),name='login'),
    path('like/<image_id>', views.like, name='like'),
    path('show',views.show,name='show'),
    path('search',views.search,name='search'),
    path('comment/<image_id>',views.comment, name = 'comment'),
    path('follow/<user_id>', views.follow, name='follow'),
    path('like/<image_id>', views.like, name='like'),
]