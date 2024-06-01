from django.contrib import admin
from .models import *

class custom_user_display (admin.ModelAdmin):
    list_display= ['username' , 'email','full_name','user_type']

    search_fields = ['username' , 'email','full_name','user_type']
    fieldsets = [
        (
            'Search',
            {'fields':['username' , 'email','full_name','user_type','first_name','last_name']}
        )
    ]
    

admin.site.register(Custom_user,custom_user_display)
admin.site.register(jobinformationModel)
admin.site.register(jobRecruitermodel)
admin.site.register(jobseekerModel)

