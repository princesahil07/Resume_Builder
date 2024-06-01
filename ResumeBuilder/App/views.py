from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request) :
    return render(request, "index.html", {})

def register(request) :
    if request.method == 'POST' :
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']

        data = User.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            email = email,
            username = username,
            password = password1
        )
        data.save()
        return redirect('login')

    return render(request, "register.html", {})

def login(request):
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None :
            auth.login(request, user)
            return redirect('resume_info')
        else :
            message = "Username and Password doest Match"
            return redirect('login')

    return render(request, "login.html", {})

@login_required
def resume_info(request) :
    if request.method == 'POST' :
        full_name = request.POST.get('full_name', '')
        designations = request.POST.get('designations', '')
        mobile_no = request.POST.get('mobile_no', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        summary = request.POST.get('summary', '')

        skill1 = request.POST.get('skill1', '')
        skill2 = request.POST.get('skill2', '')
        skill3 = request.POST.get('skill3', '')
        skill4 = request.POST.get('skill4', '')
        skill5 = request.POST.get('skill5', '')
        skill6 = request.POST.get('skill6', '')
        skill7 = request.POST.get('skill7', '')
        skill8 = request.POST.get('skill8', '')
        skill9 = request.POST.get('skill9', '')

        course_name_1 = request.POST.get('course_name_1', '')
        college_name_1 = request.POST.get('college_name_1', '')
        college_address_1 = request.POST.get('college_address_1', '')
        c_start_date_1 = request.POST.get('c_start_date_1', '')
        c_end_date_1 = request.POST.get('c_end_date_1', '')

        course_name_2 = request.POST.get('course_name_2', '')
        college_name_2 = request.POST.get('college_name_2', '')
        college_address_2 = request.POST.get('college_address_2', '')
        c_start_date_2 = request.POST.get('c_start_date_2', '')
        c_end_date_2 = request.POST.get('c_end_date_2', '')

        company_name_1 = request.POST.get('company_name_1', '')
        company_desgn_1 = request.POST.get('company_desgn_1', '')
        company_disc_1 = request.POST.get('company_disc_1', '')
        com_start_1 = request.POST.get('com_start_1', '')
        com_end_1 = request.POST.get('com_end_1', '')

        company_name_2 = request.POST.get('company_name_2', '')
        company_desgn_2 = request.POST.get('company_desgn_2', '')
        company_disc_2 = request.POST.get('company_disc_2', '')
        com_start_2 = request.POST.get('com_start_2', '')
        com_end_2 = request.POST.get('com_end_2', '')

        project_name_1 = request.POST.get('project_name_1', '')
        project_disc_1 = request.POST.get('project_disc_1', '')
        project_name_2 = request.POST.get('project_name_2', '')
        project_disc_2 = request.POST.get('project_disc_2', '')
        project_name_3 = request.POST.get('project_name_3', '')
        project_disc_3 = request.POST.get('project_disc_3', '')

        lang_1 = request.POST.get('lang_1', '')
        lang_2 = request.POST.get('lang_2', '')
        lang_3 = request.POST.get('lang_3', '')

        award_name_1 = request.POST.get('award_name_1', '')
        award_disc_1 = request.POST.get('award_disc_1', '')
        award_name_2 = request.POST.get('award_name_2', '')
        award_disc_2 = request.POST.get('award_disc_2', '')

        info = request.POST.get('info', '')

        return render(request, 'resume_download.html', {
            'full_name' : full_name, 'designations' : designations, 'mobile_no' : mobile_no,
            'email' : email, 'address' : address, 'summary' : summary, 
            'skill1' : skill1, 'skill2' : skill2, 'skill3' : skill3, 'skill4' : skill4,
            'skill5' : skill5, 'skill6' : skill6, 'skill7' : skill7, 'skill8' : skill8,
            'skill9' : skill9, 'course_name_1' : course_name_1, 'college_name_1' : college_name_1,
            'college_address_1' : college_address_1, 'c_start_date_1' : c_start_date_1,
            'c_end_date_1' : c_end_date_1, 'course_name_2' : course_name_2,
            'college_name_2' : college_name_2, 'college_address_2' : college_address_2,
            'c_start_date_2' : c_start_date_2, 'c_end_date_2' : c_end_date_2,
            'company_name_1' : company_name_1, 'company_desgn_1' : company_desgn_1,
            'company_disc_1' : company_disc_1, 'com_start_1' : com_start_1,
            'com_end_1' : com_end_1, 'company_name_2' : company_name_2, 
            'company_desgn_2' : company_desgn_2, 'company_disc_2' : company_disc_2,
            'com_start_2' : com_start_2, 'com_end_2' : com_end_2, 
            'project_name_1' : project_name_1, 'project_disc_1' : project_disc_1,
            'project_name_2' : project_name_2, 'project_disc_2' : project_disc_2,
            'project_name_3' : project_name_3, 'project_disc_3' : project_disc_3,
            'lang_1' : lang_1, 'lang_2' : lang_2, 'lang_3' : lang_3,
            'award_name_1' : award_name_1, 'award_disc_1' : award_disc_1,
            'award_name_2' : award_name_2, 'award_disc_2' : award_disc_2,
            })

    return render(request, 'resume_info.html', {})

@login_required
def logout_user(request) :
    logout(request)
    return redirect('index')