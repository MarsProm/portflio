from django.db import models
from django.urls import reverse


class Profile(models.Model):
    full_name = models.CharField(max_length=120)
    title = models.CharField(max_length=160)
    short_bio = models.CharField(max_length=255)
    about_text = models.TextField()
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    email = models.EmailField()
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    cv_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-is_active', 'full_name']

    def __str__(self):
        return self.full_name


class Project(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=220)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    github_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)
    tech_stack = models.CharField(max_length=255, help_text='Comma-separated technologies')
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-is_featured', 'display_order', '-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('projects')

