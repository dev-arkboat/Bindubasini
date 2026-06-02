from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('teachers/', views.teachers_list, name='teachers'),
    path('headmasters/', views.headmasters_list, name='headmasters'),
    path('alumni/', views.alumni_list, name='alumni'),
    path('notices/', views.notices, name='notices'),
    path('clubs/', views.clubs, name='clubs'),
    path('contact/', views.contact, name='contact'),
    path('achievements/', views.achievements, name='achievements'),
    path('developer/', views.developer, name='developer'),
]
