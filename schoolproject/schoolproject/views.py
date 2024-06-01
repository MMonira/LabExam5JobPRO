from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from backend.models import *

all_messages = {
    'signin_password': 'Password is not correct',
    'signin_username' : 'Username does not exists',
    'signin_success' : 'Signin Successfulll',
    'jobadd_success' : 'Jobadd Successfully ',
    
}


def signup(request):
    if request.method == 'POST' :
        usename = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        full_name = request.POST.get('full_name')
        user_type = request.POST.get('user_type')
        profile_photo = request.FILES.get('profile_photo')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        if password == confirm_password :
            user = Custom_user.objects.create_user(
                username = usename,
                full_name = full_name,
                user_type = user_type,
                profile_photo = profile_photo,
                gender = gender ,
                email = email,
                password = password,
                
            )
            if user.user_type == 'recruiter':
                jobRecruitermodel.objects.create(user = user)
            else:
                jobseekerModel.objects.create(user = user)
            
            user.save()
            messages.success(request,'Signup successfully')
            return redirect('signin')
        else :
            messages.warning(request, 'Password and Confirm Password did not match')
            return redirect('signup')

    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST' :
        usename = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = usename, password = password)

        if user:
            login(request,user)
            print("User is :",user.user_type)
            messages.success(request,all_messages['signin_success'])
            return redirect('dashboard')
        else:
            messages.error(request,all_messages['signin_password'])
            return redirect('signin')

    return render(request, 'signin.html')

@login_required
def dashboard(request):
    return render(request,'dashboard.html')

@login_required
def logup(request):
    logout(request)
    return redirect('signin')

@login_required
def addjob(request):
    if request.method == 'POST':
        jobtitle = request.POST.get('jobtitle')
        companyname = request.POST.get('companyname')
        companyaddress = request.POST.get('companyaddress')
        salary = request.POST.get('salary')
        worktype = request.POST.get('worktype')
        workplace = request.POST.get('workplace')
        designation = request.POST.get('designation')
        experience = request.POST.get('experience')
        companylogo = request.FILES.get('companylogo')
        
        cuUser = request.user
        

        jobData = jobinformationModel(
            job_title = jobtitle,
            company_name = companyname,
            compny_address = companyaddress,
            salary = salary,
            designation = designation,
            experience = experience,
            work_place = workplace,
            work_type = worktype,
            company_logo = companylogo,
            created_by = cuUser,
            
        )
        jobData.save()
        messages.success(request,all_messages['jobadd_success'])
        return redirect('joblist')

    return render(request,'recruiter/addjob.html')

@login_required
def appliedjob(request):
    
    return render(request,'seeker/appliedjob.html')


@login_required
def joblist(request):
    jobdata = jobinformationModel.objects.all()

    return render(request,'joblist.html',{'jobdata':jobdata})




@login_required
def profile(request):
    
    return render(request,'profile.html')



@login_required
def updatejob(request):
    pass


@login_required
def edit(request,myid):
    jobData = jobinformationModel.objects.get(id = myid)
    return render(request, 'recruiter/editjob.html')
    


@login_required
def view(request,myid):
    jobData = jobinformationModel.objects.get(id = myid)
    return render(request, 'viewjob.html')


@login_required
def delete(request,myid):
    jobData = jobinformationModel.objects.get(id = myid)
    jobData.delete()
    return redirect('joblist')
    
