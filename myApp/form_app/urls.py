from django.urls import path
from . import views
from .views import MyView, ProfileDetailView
from .views import FormUpdateView

urlpatterns = [
    path('', MyView.as_view(), name='home'),
    path('create/', views.FormCreateView.as_view(), name='create'),
    path('update/<int:person_id>/', FormUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', ProfileDetailView.as_view(), name='detail'),

]