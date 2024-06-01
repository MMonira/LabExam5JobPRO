
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',signin, name='signin'),
    path('signup/',signup, name='signup'),
    path('dashboard/',dashboard, name='dashboard'),
    path('logup/',logup, name='logup'),
    
    
    path('addjob/',addjob, name='addjob'),
    path('appliedjob/',appliedjob, name='appliedjob'),
    path('joblist/',joblist, name='joblist'),
    path('profile/',profile, name='profile'),
    
    #CRUD
    
    path('updatejob/',updatejob, name='updatejob'),
    path('view/<int:myid>',view, name='view'),
    path('delete/<int:myid>',delete, name='delete'),
    path('edit/<int:myid>',edit, name='edit'),


    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
