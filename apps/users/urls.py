from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('detail/<slug>/', views.profile_detail_view, name='profile_detail'),
]
