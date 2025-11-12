from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Project, Skill, Certification, Achievement
from .forms import ContactForm


def home(request):
    certifications_qs = Certification.objects.all()
    context = {
        'page_title': 'Home',
        'certifications': certifications_qs,
    }
    return render(request, 'portfolio/home.html', context)


def about(request):
    return render(request, 'portfolio/about.html', {'page_title': 'About'})


def skills(request):
    skills_qs = Skill.objects.all().order_by('-level')
    return render(request, 'portfolio/skills.html', {'skills': skills_qs, 'page_title': 'Skills'})


def projects(request):
    projects_qs = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects_qs, 'page_title': 'Projects'})


def certifications(request):
    certifications_qs = Certification.objects.all()
    return render(request, 'portfolio/certifications.html', {'certifications': certifications_qs, 'page_title': 'Certifications'})


def achievements(request):
    achievements_qs = Achievement.objects.all()
    return render(request, 'portfolio/achievements.html', {'achievements': achievements_qs, 'page_title': 'Achievements'})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks! Your message has been sent.')
            return redirect('contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form, 'page_title': 'Contact'})
