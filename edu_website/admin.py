from django.contrib import admin

# Registered models.
from .models import BlogPost, Testimonial, ContactMessage

admin.site.register(BlogPost)
admin.site.register(Testimonial)
admin.site.register(ContactMessage)
