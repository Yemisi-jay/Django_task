from django.urls import path
from .views import PostListView


urlpatterns = [
    path('home/', PostListView.as_view(), name='home'),
]