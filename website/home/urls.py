from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('home/',views.home, name='home'),
    path('',views.home,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('department',views.department,name='dept'),
    path('doctor',views.doctor,name='dr'),
    path('blog/',views.blog,name='blog'),
    path('pricing/',views.pricing,name='pricing'),
    path('blog/<int:yr>/<str:mon>/<int:dy>/',views.blog_single,name='blog-n'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)