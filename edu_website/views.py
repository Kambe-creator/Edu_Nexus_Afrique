from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to EduNexus Afrique!</h1>")

from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Testimonial

def home(request):
    return render(request, 'edu_website/home.html')

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'website/blog_list.html', {'posts': posts})

def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'website/blog_detail.html', {'post': post})

def testimonials(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'website/testimonials.html', {'testimonials': testimonials})

from django.http import HttpResponseRedirect
from .forms import ContactForm

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()
    return render(request, 'website/contact_us.html', {'form': form})
