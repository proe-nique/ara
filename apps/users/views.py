from django.shortcuts import render, get_object_or_404
from .models import Profile
# Create your views here.

def profile_detail_view(request, slug):
    member = get_object_or_404(Profile, slug=slug)
    template_name = 'profile_detail.html'
    context = {
        'member': member,
        'page_title': 'profile'
    }
    return render(request, template_name, context)