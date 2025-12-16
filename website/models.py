from django.db import models


# ================== Service ==================
class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=100)  # e.g. "fa fa-code"

    def __str__(self):
        return self.title


# ================== Testimonial ==================
class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200, blank=True, null=True)
    review = models.TextField()
    image = models.ImageField(upload_to="testimonials/")

    def __str__(self):
        return self.name


# ================== Project ==================
class Project(models.Model):
    CATEGORY_CHOICES = (
        ('web', 'Web Design'),
        ('graphic', 'Graphic Design'),
        ('app', 'App Development'),
    )

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="projects/")
    project_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


# ================== Team ==================
class Team(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to="team/")
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name