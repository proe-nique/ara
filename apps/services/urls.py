from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('service/detail/<slug>/', views.service_detail_view, name='service_detail'),
    path('product/detail/<slug>/', views.product_detail_view, name='product_detail'),
    
    
]