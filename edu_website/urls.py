from django.urls import path
from . import views

app_name = 'edu_website'

urlpatterns = [
    path('', views.home, name='home'),
    path('neuroaid/', views.neuroaid, name='neuroaid'),
    path('isustainme/', views.isustainme, name='isustainme'),
    path('french-konnect/', views.french_konnect, name='french_konnect'),
    path('anga/', views.anga, name='anga'),
    path('miradi/', views.miradi, name='miradi'),
     path('environmental-resilience/', views.environmental_resilience, name='environmental_resilience'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('contact/', views.contact_us, name='contact_us'),
]
