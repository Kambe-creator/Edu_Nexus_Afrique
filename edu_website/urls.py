from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Default route for the app
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('contact/', views.contact_us, name='contact_us'),
]
