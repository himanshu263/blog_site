from django.contrib import admin
from .models import Service, Testimonial, Project, Team

# ================== Service ==================
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "icon")


# ================== Testimonial ==================
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "designation", "review", "image")


# ================== Project ==================
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "project_link", "image")


# ================== Team ==================
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "designation", "image", "facebook", "twitter", "linkedin")