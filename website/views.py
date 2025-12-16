from django.shortcuts import render
from .models import Service, Project, Team, Testimonial


def home(request):
    services = Service.objects.all()
    projects = Project.objects.all()[:6]   # latest 6 projects
    teams = Team.objects.all()[:3]        # top 3 members
    testimonials = Testimonial.objects.all()[:3]  # top 3 testimonials
    return render(request, "index.html", {
        "services": services,
        "projects": projects,
        "teams": teams,
        "testimonials": testimonials,
    })


def about(request):
    teams = Team.objects.all()
    return render(request, "about.html", {"teams": teams})


def service(request):
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    return render(request, "service.html", {"services": services,"testimonials": testimonials})


def project(request):
    projects = Project.objects.all()
    return render(request, "project.html", {"projects": projects})


def team(request):
    teams = Team.objects.all()
    return render(request, "team.html", {"teams": teams})


def testimonial(request):
    testimonials = Testimonial.objects.all()
    return render(request, "testimonial.html", {"testimonials": testimonials})


def contact(request):
    return render(request, "contact.html")