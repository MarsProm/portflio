from django.shortcuts import render

from .models import Profile, Project

DEFAULT_SKILLS = [
    'SQL',
    'Django',
    'Python',
    'JavaScript',
    'CSS',
    'IA',
    'Automatizacion',
]
WHATSAPP_NUMBER = '543854932369'
WHATSAPP_MESSAGE = "Hi, I found your portfolio and I'm interested in working with you on a project."
WHATSAPP_URL = f'https://wa.me/{WHATSAPP_NUMBER}?text=Hi%2C%20I%20found%20your%20portfolio%20and%20I%E2%80%99m%20interested%20in%20working%20with%20you%20on%20a%20project.'


def get_portfolio_context():
    profile = Profile.objects.filter(is_active=True).first()
    published_projects = Project.objects.filter(is_published=True)
    featured_projects = published_projects.filter(is_featured=True)

    return {
        'profile': profile,
        'featured_projects': featured_projects,
        'projects': published_projects,
        'skills': DEFAULT_SKILLS,
        'whatsapp_url': WHATSAPP_URL,
        'whatsapp_number': WHATSAPP_NUMBER,
        'whatsapp_message': WHATSAPP_MESSAGE,
    }


def home(request):
    context = get_portfolio_context()
    return render(request, 'core/home.html', context)


def projects(request):
    context = get_portfolio_context()
    return render(request, 'core/projects.html', context)


def contact(request):
    context = get_portfolio_context()
    return render(request, 'core/contact.html', context)

