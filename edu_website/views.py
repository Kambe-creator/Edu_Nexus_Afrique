from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import BlogPost, Testimonial
from .forms import ContactForm

def home(request):
    return render(request, 'edu_website/home.html')

def home(request):
    return render(request, 'edu_website/home.html')

def neuroaid(request):
    return render(request, 'edu_website/neuroaid.html')

def isustainme(request):
    return render(request, 'edu_website/isustainme.html')

def anga(request):
    return render(request, 'edu_website/anga.html')

def french_konnect(request):
    return render(request, 'edu_website/french_konnect.html')

def miradi(request):
    return render(request, 'edu_website/miradi.html')

def environmental_resilience(request):
    return render(request, 'edu_website/environmental_resilience.html')

def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'edu_website/blog_list.html', {'posts': posts})

def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'edu_website/blog_detail.html', {'post': post})

def testimonials(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'edu_website/testimonials.html', {'testimonials': testimonials})

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()
    return render(request, 'edu_website/contact_us.html', {'form': form})
