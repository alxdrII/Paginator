from django.urls import path
from .views import get_blog_page, get_user_page

urlpatterns = [
    path('', get_blog_page),
    path('user/', get_user_page),
]
