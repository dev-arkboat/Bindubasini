from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Teacher, Headmaster, Alumni, AboutInfo, SchoolInfo, Subject, Club, SchoolBuilding, Achievement, DeveloperInfo
from notice.models import Notice


def home(request):
    teachers = Teacher.objects.filter(is_active=True)[:6]
    headmasters = Headmaster.objects.filter(is_current=True)
    notices = Notice.objects.filter(is_published=True)[:5]
    achievements = Achievement.objects.all()[:6]
    clubs = Club.objects.all()[:6]
    alumni_list = Alumni.objects.all()[:6]
    context = {
        'teachers': teachers,
        'headmasters': headmasters,
        'notices': notices,
        'achievements': achievements,
        'clubs': clubs,
        'alumni_list': alumni_list,
    }
    return render(request, 'school/home.html', context)


def about(request):
    about_sections = AboutInfo.objects.filter(is_published=True)
    buildings = SchoolBuilding.objects.all()
    subjects = Subject.objects.all()
    context = {
        'about_sections': about_sections,
        'buildings': buildings,
        'subjects': subjects,
    }
    return render(request, 'school/about.html', context)


def teachers_list(request):
    teachers = Teacher.objects.filter(is_active=True)
    subjects = Subject.objects.all()
    context = {
        'teachers': teachers,
        'subjects': subjects,
    }
    return render(request, 'school/teachers.html', context)


def headmasters_list(request):
    headmasters = Headmaster.objects.all()
    context = {'headmasters': headmasters}
    return render(request, 'school/headmasters.html', context)


def alumni_list(request):
    alumni = Alumni.objects.all()
    context = {'alumni': alumni}
    return render(request, 'school/alumni.html', context)


def notices(request):
    all_notices = Notice.objects.filter(is_published=True)
    important_notices = all_notices.filter(is_important=True)
    general_notices = all_notices.filter(is_important=False)
    context = {
        'important_notices': important_notices,
        'general_notices': general_notices,
    }
    return render(request, 'school/notices.html', context)


def clubs(request):
    all_clubs = Club.objects.all()
    context = {'clubs': all_clubs}
    return render(request, 'school/clubs.html', context)


def developer(request):
    dev = DeveloperInfo.objects.filter(is_active=True).first()
    context = {'dev': dev}
    return render(request, 'school/developer.html', context)


def contact(request):
    from .models import ContactMessage
    if request.method == 'POST':
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone', ''),
            subject=request.POST.get('subject'),
            message=request.POST.get('message'),
        )
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')
    context = {}
    return render(request, 'school/contact.html', context)


def achievements(request):
    achievements_list = Achievement.objects.all()
    context = {'achievements': achievements_list}
    return render(request, 'school/achievements.html', context)
