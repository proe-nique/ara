from multiprocessing import get_context
from django.urls import reverse
from django.shortcuts import render , get_object_or_404
from apps.services.models import Service, Product
from apps.users.models import Profile
from .models import Review
from .forms import ReviewForm
from django.views.generic import CreateView
# Create your views here.




def home_view(request):
    template_name = 'home.html'
    services = Service.objects.all()
    products = Product.objects.all()
    members = Profile.objects.all()
    reviews = Review.objects.all()[:3]
    
    context = {
        'page_title':'home',
        'services':services,
        'products':products,
        'members':members,
        'reviews':reviews,
    }
    return render(request, template_name, context)

def send_email(request):
    pass


class ReviewCreateView(CreateView):
    model = Review
    template_name = "review.html"
    form_class = ReviewForm
    success_url = 'home:home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'review us'
        return context

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home:home')
    
