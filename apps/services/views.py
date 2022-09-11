from django.shortcuts import render , get_object_or_404
from .models import Service, Product

# Create your views here.


def service_detail_view(request, slug):
    template_name = 'service_detail.html'
    service = get_object_or_404(Service, slug=slug)
    
    context = {
        'page_title':service.name,
        'service':service,
    }
    
   
    return render(request, template_name, context) 

#product detail view
def product_detail_view(request, slug):
    template_name = 'product_detail.html'
    product = get_object_or_404(Product, slug=slug)
    
    context = {
        'page_title':'product_detail',
        'product': product,
        
    }
    return render(request, template_name, context)