from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('resume', views.resume, name='resume'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('blog', views.blogs, name='blogs'),
    path('contact', views.contact, name='contact'),
]
