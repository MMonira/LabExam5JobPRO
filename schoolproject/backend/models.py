from django.db import models
from django.contrib.auth.models import AbstractUser

class Custom_user (AbstractUser):
    USER = [
        ('recruiter','Recruiter'),('seeker','Seeker')
    ]
    GENDER= [
        ('male','Male'),('female','Female'),('other','Other')
    ]
    
    user_type = models.CharField(choices=USER , max_length= 40)
    profile_photo = models.ImageField (upload_to='static/media')
    gender = models.CharField(choices=GENDER , max_length=40)
    full_name = models.CharField(max_length=100,null=True)


class jobinformationModel (models.Model):
    job_title = models.CharField(max_length=100, null=True)
    company_name = models.CharField(max_length=100, null=True)
    compny_address = models.CharField(max_length=100, null=True)
    salary = models.CharField(max_length=100, null=True)
    designation = models.CharField(max_length=100, null=True)
    experience = models.CharField(max_length=100, null=True)
    TYPE = [
        ("full_time","Full time") , ("part_time","Part time") 
    ]
    PALCE = [
        ("remote","Remote") , ("onsite","Onsite") 
    ]
    work_place = models.CharField(choices=PALCE, max_length=100, null=True)
    work_type = models.CharField(choices=TYPE , max_length=100, null=True)
    company_logo = models.ImageField(upload_to='static/media', null=True)
    created_by = models.ForeignKey(Custom_user , on_delete=models.CASCADE )


    def __str__(self):
        return self.job_title + ' '+ self.created_by.full_name
    
    
class jobRecruitermodel(models.Model):
    user = models.OneToOneField(Custom_user, on_delete=models.CASCADE , related_name='recruitermodel')
    company_name = models.CharField(max_length=100, null=True,blank=True)
    designation = models.CharField(max_length=100, null=True,blank=True)
    present_address = models.CharField(max_length=100, null=True,blank=True)
    #contact information
    phone = models.IntegerField(null=True,blank=True)
    email = models.CharField(max_length=100, null=True,blank=True)
    instragram = models.CharField(max_length=100, null=True,blank=True)
    # basic information
    fathers_name = models.CharField(max_length=100, null=True,blank=True)
    
    hobby = models.CharField(max_length=100, null=True,blank=True)
    languages = models.CharField(max_length=200, null=True,blank=True)
    
    def __str__(self):
        return f'{self.user.user_type} {self.user.username}'
    
    
    
class jobseekerModel(models.Model):
    user = models.OneToOneField(Custom_user, on_delete=models.CASCADE , related_name='seekermodel')
    qualifications = models.CharField(max_length=200, null=True,blank=True)
    experience = models.CharField(max_length=100, null=True,blank=True)
    skills = models.CharField(max_length=200, null=True,blank=True)
    #basic information
    fathers_name = models.CharField(max_length=200, null=True,blank=True)
    hobby = models.CharField(max_length=200, null=True,blank=True)
    languages = models.CharField(max_length=200, null=True,blank=True)
    #contact information
    mobile = models.CharField(max_length=20, null=True,blank=True)
    email = models.CharField(max_length=100, null=True,blank=True)
    address = models.CharField(max_length=200, null=True,blank=True)
    #education information
    department = models.CharField(max_length=200, null=True,blank=True)
    education_year = models.CharField(max_length=200, null=True,blank=True)
    education_institute = models.CharField(max_length=200, null=True,blank=True)
    #workexperience information
    position = models.CharField(max_length=200, null=True,blank=True)
    institute_name = models.CharField(max_length=200, null=True,blank=True)
    duration = models.CharField(max_length=200, null=True,blank=True)
    
    def __str__(self):
        return f'{self.user.full_name} {self.user.username}'
    