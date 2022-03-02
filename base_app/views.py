from django.http import HttpResponse
from datetime import *
from django.shortcuts import redirect, render
from django.http import HttpResponse
from base_app.models import *
from core import settings
import json
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


#--------------------ADMIN MODULE--------------------------


def login(request):
    if request.method =='POST':
        design=designation.objects.get(designation="manager")
        if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=design.id).exists():
            
            member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['m_id'] = member.designation_id
            request.session['usernamets1'] = member.fullname
            request.session['usernamehr2'] = member.branch_id
            request.session['m_id'] = member.id 
            mem=user_registration.objects.filter(id= member.id)
            Num = user_registration.objects.count()
            Num1 = project.objects.count()
            Trainer = designation.objects.get(designation='Trainer')
            trcount=user_registration.objects.filter(designation=Trainer).count()
            return render(request,'MAN_profiledash.html',{'mem':mem,'num':Num,'Num1':Num1,'trcount':trcount})

        Adm1=designation.objects.get(designation="Admin")
        if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=Adm1.id).exists():
            
            member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['Adm_id'] = member.designation_id
            request.session['usernamets1'] = member.fullname
            request.session['usernamehr2'] = member.branch_id
            request.session['Adm_id'] = member.id 
            Adm=user_registration.objects.filter(id= member.id)
            Num = user_registration.objects.count()
            Num1 = project.objects.count()
            Trainer = designation.objects.get(designation='Trainer')
            trcount=user_registration.objects.filter(designation=Trainer).count()
            return render(request,'BRadmin_profiledash.html',{'num':Num,'Num1':Num1,'Adm':Adm,'trcount':trcount})
            
        else:
            message = "invalid username or password"
            return render(request ,'login.html',{'message':message})
    return render(request, 'login.html')


def Admlogout(request):
    if 'Adm_id' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/') 

def Mnlogout(request):
    if 'm_id' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')


#***********************anandu*****************************************
def MAN_index(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    return render(request,'MAN_index.html',{'mem':mem})

def MAN_profiledash(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    Num = user_registration.objects.count()
    Num1 = project.objects.count()
    Trainer = designation.objects.get(designation='Trainer')
    trcount=user_registration.objects.filter(designation=Trainer).count()
    Man1 = designation.objects.get(designation='Manager')
    Man2 = user_registration.objects.filter(designation = Man1)
    return render(request,'MAN_profiledash.html',{'Man1':Man2,'mem':mem,'num':Num,'trcount':trcount,'Num1':Num1})   

def MAN_employees(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    Dept = department.objects.all()
    return render(request,'MAN_employees.html',{'mem':mem,'Dept':Dept})
def MAN_python(request,id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    Dept = department.objects.get(id = id)
    deptid=id
    mem = user_registration.objects.filter(id=m_id)
    Desig = designation.objects.all()
    return render(request,'MAN_python.html',{'mem':mem,'Desig':Desig,'Dept':Dept,'dept_id':deptid})

def MAN_projectman(request,id,did):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    mem = user_registration.objects.filter(id=m_id)
    project_name = project.objects.all()
    Project_man= designation.objects.get(id = id)
    Project_man_data=user_registration.objects.filter(designation=Project_man).filter(department=did)
    return render(request,'MAN_projectman.html',{'pro_man_data':Project_man_data,'mem':mem,'project_name':project_name,'Project_man':Project_man})
def MAN_proname(request,id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    Project_man_data = user_registration.objects.get(id = id)
    return render(request,'MAN_proname.html',{'pro_man_data':Project_man_data,'mem':mem})
def MAN_proinvolve(request,id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    Pro_data = project.objects.filter(user_id = id)
    return render(request,'MAN_proinvolve.html',{'pro_data':Pro_data,'mem':mem})

def MAN_promanatten(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        id = id
        return render(request, 'MAN_promanatten.html',{'mem':mem,'id':id})
    else:
        return redirect('/')

def MAN_promanattendsort(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        id = id
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            # mem1 = attendance.objects.raw('select * from app_attendance where user_id and date between "'+fromdate+'" and "'+todate+'"')
            mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id = id)
        return render(request, 'MAN_promanattendsort.html',{'mem1':mem1,'mem':mem,'id':id})
    else:
        return redirect('/')     


def BRadmin_index(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.filter(id=Adm_id)
    return render(request,'BRadmin_index.html',{'mem':mem})
    
def BRadmin_profiledash(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id)
    Num = user_registration.objects.count()
    Num1 = project.objects.count()
    
    Trainer = designation.objects.get(designation='Trainer')
    trcount=user_registration.objects.filter(designation=Trainer).count()
    Man1 = designation.objects.get(designation='Manager')
    Man2 = user_registration.objects.filter(designation = Man1)
    return render(request,'BRadmin_profiledash.html',{'Num1':Num1,'Man1':Man2,'Adm':Adm,'num':Num,'trcount':trcount})   

def BRadmin_employees(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id)
    Dept = department.objects.all()
    return render(request,'BRadmin_employees1.html',{'Adm':Adm,'Dept':Dept})

def BRadmin_python(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    Dept = department.objects.get(id = id)
    deptid=id
    Adm = user_registration.objects.filter(id=Adm_id)
    Desig = designation.objects.all()
    return render(request,'BRadmin_python.html',{'Adm':Adm,'Desig':Desig,'Dept':Dept,'dept_id':deptid})
    
def BRadmin_projectman(request,id,did):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    Adm = user_registration.objects.filter(id=Adm_id)
    project_name = project.objects.all()
    Project_man= designation.objects.get(id = id)
    Project_man_data=user_registration.objects.filter(designation=Project_man).filter(department=did)
    return render(request,'BRadmin_projectman.html',{'pro_man_data':Project_man_data,'Adm':Adm,'project_name':project_name,'Project_man':Project_man})
def BRadmin_proname(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id)
    Project_man_data = user_registration.objects.get(id = id)
    return render(request,'BRadmin_proname.html',{'pro_man_data':Project_man_data,'Adm':Adm})
def BRadmin_proinvolve(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id)
    Pro_data = project.objects.filter(user_id = id)
    return render(request,'BRadmin_proinvolve.html',{'pro_data':Pro_data,'Adm':Adm})

def BRadmin_promanatten(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        id = id
        return render(request, 'BRadmin_promanatten.html',{'Adm':Adm,'id':id})
    else:
        return redirect('/')

def BRadmin_promanattendsort(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        id = id
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            # mem1 = attendance.objects.raw('select * from app_attendance where user_id and date between "'+fromdate+'" and "'+todate+'"')
            mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id = id)
        return render(request, 'BRadmin_promanattendsort.html',{'mem1':mem1,'Adm':Adm,'id':id})
    else:
        return redirect('/') 







#***********************praveen************************
def BRadmin_trainerstable(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        variable="dummy"
    Adm = user_registration.objects.filter(id=Adm_id)
    Trainer = designation.objects.get(designation='Trainer')
    trainers_data=user_registration.objects.filter(designation=Trainer)
    topics=topic.objects.all()
    return render(request,'BRadmin_trainerstable.html',{'Adm':Adm,'trainers_data':trainers_data,'topics':topics})
def BRadmin_Training(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        variable="dummy"
    Adm = user_registration.objects.filter(id=Adm_id)
    #team=create_team.objects.filter(user_id=id)
    #return render(request,'BRadmin_Training.html',{'team':team})
        #team=create_team.objects.all()
    user=user_registration.objects.filter(id=id)
    team=create_team.objects.all()
    return render(request,'BRadmin_Training.html',{'team':team,'user':user,'Adm':Adm})
def BRadmin_trainingteam1(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        variable="dummy"
    Adm = user_registration.objects.filter(id=Adm_id)
    id=id
    Trainee = designation.objects.get(designation='Trainee')
    num=user_registration.objects.filter(designation=Trainee).filter(team=id).count()
    num1=topic.objects.filter(team=id).count()
    return render(request,'BRadmin_trainingteam1.html',{'id':id,'num':num,'num1':num1,'Adm':Adm})
def BRadmin_traineestable(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        variable="dummy"
    Adm = user_registration.objects.filter(id=Adm_id)
    Trainee = designation.objects.get(designation='Trainee')
    trainees_data=user_registration.objects.filter(designation=Trainee).filter(team=id)
    return render(request,'BRadmin_traineestable.html',{'trainees_data':trainees_data,'Adm':Adm}) 
def BRadmin_trainingprofile(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        variable="dummy"
    Adm = user_registration.objects.filter(id=Adm_id)
    trainees_data=user_registration.objects.get(id=id)
    #Trainee = designation.objects.get(designation='Trainee')
    #trainees_data=user_registration.objects.filter(designation=Trainee)
    user=user_registration.objects.get(id=id)
    num=trainer_task.objects.filter(user=user).filter(status='Completed').count()
    return render(request,'BRadmin_trainingprofile.html',{'trainees_data':trainees_data,'num':num,'Adm':Adm})
def BRadmin_completedtasktable(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        variable="dummy"
    Adm = user_registration.objects.filter(id=Adm_id)
    user=user_registration.objects.get(id=id)
    task=trainer_task.objects.filter(user=user)
    return render(request,'BRadmin_completedtasktable.html',{'task_data':task,'Adm':Adm})
def BRadmin_topictable(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        variable="dummy"
    Adm = user_registration.objects.filter(id=Adm_id)
    topics=topic.objects.filter(team=id)
    return render(request,'BRadmin_topictable.html',{'topics':topics,'Adm':Adm})

def MAN_trainerstable(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        variable="dummy"
    mem = user_registration.objects.filter(id=m_id)
    Trainer = designation.objects.get(designation='Trainer')
    trainers_data=user_registration.objects.filter(designation=Trainer)
    topics=topic.objects.all()
    return render(request,'MAN_trainerstable.html',{'trainers_data':trainers_data,'topics':topics,'mem':mem})
def MAN_Training(request,id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        variable="dummy"
    mem = user_registration.objects.filter(id=m_id)
    #team=create_team.objects.filter(user_id=id)
    #return render(request,'BRadmin_Training.html',{'team':team})
        #team=create_team.objects.all()
    user=user_registration.objects.filter(id=id)
    team=create_team.objects.all()
    return render(request,'MAN_Training.html',{'team':team,'user':user,'mem':mem})
def MAN_trainingteam1(request,id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        variable="dummy"
    mem = user_registration.objects.filter(id=m_id)
    id=id
    Trainee = designation.objects.get(designation='Trainee')
    num=user_registration.objects.filter(designation=Trainee).filter(team=id).count()
    num1=topic.objects.filter(team=id).count()
    return render(request,'MAN_trainingteam1.html',{'id':id,'num':num,'num1':num1,'mem':mem})
def MAN_traineestable(request,id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        variable="dummy"
    mem = user_registration.objects.filter(id=m_id)
    Trainee = designation.objects.get(designation='Trainee')
    trainees_data=user_registration.objects.filter(designation=Trainee).filter(team=id)
    return render(request,'MAN_traineestable.html',{'trainees_data':trainees_data,'mem':mem}) 
def MAN_trainingprofile(request,id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        variable="dummy"
    mem = user_registration.objects.filter(id=m_id)
    trainees_data=user_registration.objects.get(id=id)
    #Trainee = designation.objects.get(designation='Trainee')
    #trainees_data=user_registration.objects.filter(designation=Trainee)
    user=user_registration.objects.get(id=id)
    num=trainer_task.objects.filter(user=user).filter(status='Completed').count()
    return render(request,'MAN_trainingprofile.html',{'trainees_data':trainees_data,'num':num,'mem':mem})
def MAN_completedtasktable(request,id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        variable="dummy"
    mem = user_registration.objects.filter(id=m_id)
    user=user_registration.objects.get(id=id)
    task=trainer_task.objects.filter(user=user)
    return render(request,'MAN_completedtasktable.html',{'task_data':task,'mem':mem})
def MAN_topictable(request,id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        variable="dummy"
    mem = user_registration.objects.filter(id=m_id)
    topics=topic.objects.filter(team=id)
    return render(request,'MAN_topictable.html',{'topics':topics,'mem':mem})







#*******************    anwar     ****************************

def BRadmin_View_Trainers(request,id,did):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        variable="dummy"
    Adm = user_registration.objects.filter(id=Adm_id)
    
    projectname=project.objects.all()
    trainer=designation.objects.get(id=id)
    userreg=user_registration.objects.filter(designation=trainer).filter(department=did)
    return render(request,'BRadmin_View_Trainers.html', {'Adm':Adm,'user_registration':userreg, 'project':projectname})


def BRadmin_View_Trainerprofile(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        variable="dummy"
    Adm = user_registration.objects.filter(id=Adm_id)
    userreg=user_registration.objects.get(id=id)
    return render(request,'BRadmin_View_Trainerprofile.html', {'Adm':Adm,'user_registration':userreg})


def BRadmin_View_Currenttraineesoftrainer(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        variable="dummy"
    Adm = user_registration.objects.filter(id=Adm_id)
    user=user_registration.objects.filter(id=id)
    trainee=designation.objects.get(designation='Trainee')
    user2=user_registration.objects.filter(designation=trainee)
    
    return render(request,'BRadmin_View_Currenttraineesoftrainer.html',{'Adm':Adm,'user_registration':user,'user_registration2':user2})

def BRadmin_View_Previoustraineesoftrainer(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        variable="dummy"
    Adm = user_registration.objects.filter(id=Adm_id)
    user=user_registration.objects.filter(id=id)
    trainee=designation.objects.get(designation='Trainee')
    user2=user_registration.objects.filter(designation=trainee)

    return render(request,'BRadmin_View_Previoustraineesoftrainer.html',{'Adm':Adm,'user_registration':user,'user_registration2':user2})

def BRadmin_View_Currenttraineeprofile(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        variable="dummy"
    Adm = user_registration.objects.filter(id=Adm_id)
    userreg=user_registration.objects.get(id=id)
    return render(request,'BRadmin_View_Currenttraineeprofile.html', {'Adm':Adm,'user_registration':userreg})

def BRadmin_View_Currenttraineetasks(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        variable="dummy"
    Adm = user_registration.objects.filter(id=Adm_id)
    # user=user_registration.objects.get(id=id)
    tasks=trainer_task.objects.filter(user=id)
    return render(request,'BRadmin_View_Currenttraineetasks.html',{'Adm':Adm,'trainer_task':tasks})

def BRadmin_View_Currenttraineeattendance(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        variable="dummy"
    Adm = user_registration.objects.filter(id=Adm_id)
    usr=user_registration.objects.get(id=id)
    return render(request,'BRadmin_View_Currenttraineeattendance.html', {'Adm':Adm,'user_registration':usr})

def BRadmin_View_Previoustraineeprofile(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        variable="dummy"
    Adm = user_registration.objects.filter(id=Adm_id)
    usr=user_registration.objects.get(id=id)
    return render(request,'BRadmin_View_Previoustraineeprofile.html', {'Adm':Adm,'user_registration':usr})

def BRadmin_View_Previoustraineetasks(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        variable="dummy"
    Adm = user_registration.objects.filter(id=Adm_id)
    user=user_registration.objects.get(id=id)
    tasks=trainer_task.objects.filter(user=user)
    return render(request,'BRadmin_View_Previoustraineetasks.html',{'Adm':Adm,'trainer_task':tasks})

def BRadmin_View_Previoustraineeattendance(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        variable="dummy"
    Adm = user_registration.objects.filter(id=Adm_id)
    usr=user_registration.objects.get(id=id)
    return render(request,'BRadmin_View_Previoustraineeattendance.html', {'Adm':Adm,'user_registration':usr})


def BRadmin_View_Trainerattendance(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        variable="dummy"
    Adm = user_registration.objects.filter(id=Adm_id)
    usr=user_registration.objects.get(id=id)
    return render(request,'BRadmin_View_Trainerattendance.html', {'Adm':Adm,'user_registration':usr})


def BRadmin_ViewTrainerattendancesort(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        variable="dummy"
    Adm = user_registration.objects.filter(id=Adm_id)
    usr=user_registration.objects.get(id=id)
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate') 
        adata =attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
        
    return render(request,'BRadmin_View_Trainerattendanceview.html',{'Adm':Adm,'adata':adata,'user_registration':usr})

def BRadmin_ViewCurrenttraineeattendancesort(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        variable="dummy"
    Adm = user_registration.objects.filter(id=Adm_id)
    usr=user_registration.objects.get(id=id)
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate') 
        adata =attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
        
    return render(request,'BRadmin_View_Currenttraineeattendanceview.html',{'Adm':Adm,'adata':adata,'user_registration':usr})




def BRadmin_ViewPrevioustraineeattendancesort(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        variable="dummy"
    Adm = user_registration.objects.filter(id=Adm_id)
    usr=user_registration.objects.get(id=id)
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate') 
        adata = attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
        
    return render(request,'BRadmin_View_Previoustraineeattendanceview.html',{'Adm':Adm,'adata':adata,'user_registration':usr})


def admin_page1(request):
    if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
    else:
        variable="dummy"
    Adm = user_registration.objects.filter(id=Adm_id)
    dpt=department.objects.all()
    dsg=designation.objects.all()
    userreg=user_registration.objects.all()
    return render(request,'BRadmin_attendance.html', {'Adm':Adm,'department':dpt,'designation':dsg,'user_registration':userreg})  



def admin_page3(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        variable="dummy"
    Adm = user_registration.objects.filter(id=Adm_id)
    if request.method == "POST":
        empname1=request.POST.get('empname')
        atten=attendance.objects.all()
    return render(request,'BRadmin_attendanceshow.html',{'Adm':Adm,'atten':atten,'empname1':empname1}) 
   



def admin_desi(request):   
    dept_id = request.GET.get('dept_id')
    departments=department.objects.all()
    Desig = designation.objects.all()
    return render(request, 'BRadmin_designation.html', {'Desig': Desig,'departments':departments})



def admin_emp(request):   
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    dept=department.objects.filter(id=dept_id)
    desi=designation.objects.filter(id=desig_id)
    user=user_registration.objects.filter(designation_id=dept_id)
    print(dept)
    print(desi)
    return render(request, 'BRadmin_employee.html',{'user':user,'dept':dept,'desi':desi})



def MAN_View_Trainers(request,id,did):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        variable="dummy"
    mem = user_registration.objects.filter(id=m_id)
    projectname=project.objects.all()
    trainer=designation.objects.get(id=id)
    userreg=user_registration.objects.filter(designation=trainer).filter(department=did)
    return render(request,'MAN_View_Trainers.html', {'mem':mem,'user_registration':userreg, 'project':projectname})


def MAN_View_Trainerprofile(request,id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        variable="dummy"
    mem = user_registration.objects.filter(id=m_id)
    userreg=user_registration.objects.get(id=id)
    return render(request,'MAN_View_Trainerprofile.html', {'mem':mem,'user_registration':userreg})


def MAN_View_Currenttraineesoftrainer(request,id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        variable="dummy"
    mem = user_registration.objects.filter(id=m_id)
   
    user=user_registration.objects.filter(id=id)
    trainee=designation.objects.get(designation='Trainee')
    user2=user_registration.objects.filter(designation=trainee)
    
    return render(request,'MAN_View_Currenttraineesoftrainer.html',{'mem':mem,'user_registration':user,'user_registration2':user2})

def MAN_View_Previoustraineesoftrainer(request,id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        variable="dummy"
    mem = user_registration.objects.filter(id=m_id)
   
    user=user_registration.objects.filter(id=id)
    trainee=designation.objects.get(designation='Trainee')
    user2=user_registration.objects.filter(designation=trainee)

    return render(request,'MAN_View_Previoustraineesoftrainer.html',{'mem':mem,'user_registration':user,'user_registration2':user2})

def MAN_View_Currenttraineeprofile(request,id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        variable="dummy"
    mem = user_registration.objects.filter(id=m_id)
    userreg=user_registration.objects.get(id=id)
    return render(request,'MAN_View_Currenttraineeprofile.html', {'mem':mem,'user_registration':userreg})

def MAN_View_Currenttraineetasks(request,id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        variable="dummy"
    mem = user_registration.objects.filter(id=m_id)
    # user=user_registration.objects.get(id=id)
    tasks=trainer_task.objects.filter(user=id)
    return render(request,'MAN_View_Currenttraineetasks.html',{'mem':mem,'trainer_task':tasks})

def MAN_View_Currenttraineeattendance(request,id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        variable="dummy"
    mem = user_registration.objects.filter(id=m_id)
    usr=user_registration.objects.get(id=id)
    return render(request,'MAN_View_Currenttraineeattendance.html', {'mem':mem,'user_registration':usr})

def MAN_View_Previoustraineeprofile(request,id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        variable="dummy"
    mem = user_registration.objects.filter(id=m_id)
    usr=user_registration.objects.get(id=id)
    return render(request,'MAN_View_Previoustraineeprofile.html', {'mem':mem,'user_registration':usr})

def MAN_View_Previoustraineetasks(request,id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        variable="dummy"
    mem = user_registration.objects.filter(id=m_id)
    user=user_registration.objects.get(id=id)
    tasks=trainer_task.objects.filter(user=user)
    return render(request,'MAN_View_Previoustraineetasks.html',{'mem':mem,'trainer_task':tasks})

def MAN_View_Previoustraineeattendance(request,id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        variable="dummy"
    mem = user_registration.objects.filter(id=m_id)
    usr=user_registration.objects.get(id=id)
    return render(request,'MAN_View_Previoustraineeattendance.html', {'mem':mem,'user_registration':usr})

def MAN_View_Trainerattendance(request,id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        variable="dummy"
    mem = user_registration.objects.filter(id=m_id)
    usr=user_registration.objects.get(id=id)
    return render(request,'MAN_View_Trainerattendance.html', {'mem':mem,'user_registration':usr})


def MAN_ViewTrainerattendancesort(request,id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        variable="dummy"
    mem = user_registration.objects.filter(id=m_id)
    usr=user_registration.objects.get(id=id)
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate') 
        adata =attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
        
    return render(request,'MAN_View_Trainerattendanceview.html',{'mem':mem,'adata':adata,'user_registration':usr})


def MAN_ViewCurrenttraineeattendancesort(request,id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        variable="dummy"
    mem = user_registration.objects.filter(id=m_id)
    usr=user_registration.objects.get(id=id)
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate') 
        adata =attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
        
    return render(request,'MAN_View_Currenttraineeattendanceview.html',{'mem':mem,'adata':adata,'user_registration':usr})

def MAN_ViewPrevioustraineeattendancesort(request,id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        variable="dummy"
    mem = user_registration.objects.filter(id=m_id)
    usr=user_registration.objects.get(id=id)
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate') 
        adata = attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
        
    return render(request,'MAN_View_Previoustraineeattendanceview.html',{'mem':mem,'adata':adata,'user_registration':usr})


def MAN_dev_attendance(request):
    return render(request,'MAN_dev_attendance.html')    

def man_page1(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        variable="dummy"
    mem = user_registration.objects.filter(id=m_id)
 
    dpt=department.objects.all()
    dsg=designation.objects.all()
    userreg=user_registration.objects.all()
    return render(request,'MAN_attendance.html', {'mem':mem,'department':dpt,'designation':dsg,'user_registration':userreg})  

def man_page3(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        variable="dummy"
    mem = user_registration.objects.filter(id=m_id)
    
    if request.method == "POST":
        empname1=request.POST.get('empname')
        atten=attendance.objects.all()
    return render(request,'MAN_attendanceshow.html',{'mem':mem,'atten':atten,'empname1':empname1}) 
   
def man_desi(request):   
    dept_id = request.GET.get('dept_id')
    departments=department.objects.all()
    Desig = designation.objects.all()
    return render(request, 'MAN_designation.html', {'Desig': Desig,'departments':departments})


def man_emp(request):   
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    dept=department.objects.filter(id=dept_id)
    desi=designation.objects.filter(id=desig_id)
    user=user_registration.objects.filter(designation_id=dept_id)
    print(dept)
    print(desi)
    return render(request, 'MAN_employee.html',{'user':user,'dept':dept,'desi':desi})

#************************  anwar end  *********************************************





 # current projects- sharon
def BRadmin_pythons(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id)
    project_details = project.objects.all()
    return render(request,'BRadmin_projects.html',{'proj_det':project_details,'Adm':Adm})

def BRadmin_dept(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id)
    project_details = project.objects.all()
    depart =department.objects.all()
    return render(request,'BRadmin_dept.html',{'proj_det':project_details,'department':depart,'Adm':Adm})

    
# def BRadmin_profiledash(request):
#     Num= project.objects.count()
#     project_details = project.objects.all()
#     return render(request,'BRadmin_profiledash.html',{'proj_det':project_details,'num':Num})

def BRadmin_projects(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id)
    Num= project.objects.filter(status='accepted').filter(department=id).count()
    num= project.objects.filter(status='completed').filter(department=id).count()
    project_details = project.objects.all()
    depart =department.objects.get(id=id)
    id=id
    return render(request,'BRadmin_projects.html',{'proj_det':project_details,'num':Num,'Num':num,'department':depart,'id':id,'Adm':Adm})
 

def BRadmin_proj_list(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id)
    project_details = project.objects.filter(department=id)
    print (project_details.count())
    return render(request,'BRadmin_proj_list.html',{'proj_det':project_details,'Adm':Adm})

def BRadmin_proj_det(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id)
    project_details = project.objects.get(id=id)
    return render(request,'BRadmin_proj_det.html',{'proj_det':project_details,'Adm':Adm})

def BRadmin_proj_mngrs(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id)
    project_details = project.objects.get(id=id)
    return render(request,'BRadmin_proj_mngrs.html',{'proj_det':project_details,'Adm':Adm})

def BRadmin_proj_mangrs1(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id)
    project_details = project.objects.get(id=id) 
    return render(request,'BRadmin_proj_mangrs1.html',{'proj_det':project_details,'Adm':Adm})

def BRadmin_proj_mangrs2(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id)
    project_details = project.objects.get(id=id) 
    project_task = project_taskassign.objects.all()
    return render(request,'BRadmin_proj_mangrs2.html',{'proj_task':project_task,'proj_det':project_details,'Adm':Adm})

def BRadmin_daily_report(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id) 
    project_task = project_taskassign.objects.get(id=id)
    tester =tester_status.objects.all()
    return render(request,'BRadmin_daily_report.html',{'proj_task':project_task,'test':tester,'Adm':Adm})

def BRadmin_developers(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id)
    project_details = project.objects.get(id=id) 
    project_task = project_taskassign.objects.filter(tl_id = id)
    progress_bar= tester_status.objects.all()
    return render(request,'BRadmin_developers.html',{'proj_task':project_task,'proj_det':project_details,'prog_status':progress_bar,'Adm':Adm})


# completed projects- subeesh
 
def BRadmin_proj_cmpltd_new(request, id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id)
    project_details=project.objects.filter(department=id)
    print (project_details.count())
    return render(request,'BRadmin_proj_cmpltd_show.html',{'project': project_details,'Adm':Adm})


def BRadmin_cmpltd_proj_det_new(request, id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id)
    project_details = project.objects.get(id=id)
    return render(request,'BRadmin_cmpltd_proj_det_show.html',{'project': project_details,'Adm':Adm})

def BRadmin_proj_mngrs_new(request, id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id)
    project_details = project.objects.get(id=id)
    return render(request,'BRadmin_proj_mngrs_show.html', {'project': project_details,'Adm':Adm})

def BRadmin_proj_mangrs1_new(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id)
    project_details = project.objects.get(id=id)
    return render(request,'BRadmin_proj_mangrs1_show.html', {'project': project_details,'Adm':Adm})

def BRadmin_proj_mangrs2_new(request, id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id)
    project_details = project.objects.get(id=id)
    project_task = project_taskassign.objects.all()
    return render(request,'BRadmin_proj_mangrs2_show.html', {'project':project_details,'project_taskassign':project_task,'Adm':Adm})

def BRadmin_developers_new(request, id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id)
    project_details = project.objects.get(id=id)
    project_task = project_taskassign.objects.filter(tl_id = id)
    progress_bar= tester_status.objects.all()
    return render(request,'BRadmin_developers_show.html', {'project':project_details,'project_taskassign':project_task,'prog_status':progress_bar,'Adm':Adm})

def BRadmin_daily_report_new(request, id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id)
    project_task = project_taskassign.objects.get(id=id)
    tester = tester_status.objects.all()
    return render(request,'BRadmin_daily_report_show.html', {'project':project_task,'tester_status':tester,'Adm':Adm})


 # current projects-sharon -manager module
def MAN_pythons(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    project_details = project.objects.all()
    return render(request,'MAN_projects.html',{'proj_det':project_details,'mem':mem})

def MAN_dept(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    project_details = project.objects.all()
    depart =department.objects.all()
    return render(request,'MAN_dept.html',{'proj_det':project_details,'department':depart,'mem':mem})

    
# def MAN_profiledash(request):
#     Num= project.objects.count()
#     project_details = project.objects.all()
#     return render(request,'MAN_profiledash.html',{'proj_det':project_details,'num':Num})

def MAN_projects(request,id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    Num= project.objects.filter(status='accepted').filter(department=id).count()
    num= project.objects.filter(status='completed').filter(department=id).count()
    project_details = project.objects.all()
    depart =department.objects.get(id=id)
    id=id
    return render(request,'MAN_projects.html',{'proj_det':project_details,'num':Num,'Num':num,'department':depart,'id':id,'mem':mem})
 

def MAN_proj_list(request,id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    project_details = project.objects.filter(department=id)
    print (project_details.count())
    return render(request,'MAN_proj_list.html',{'proj_det':project_details,'mem':mem})

def MAN_proj_det(request,id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    project_details = project.objects.get(id=id)
    return render(request,'MAN_proj_det.html',{'proj_det':project_details,'mem':mem})

def MAN_proj_mngrs(request,id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    project_details = project.objects.get(id=id)
    return render(request,'MAN_proj_mngrs.html',{'proj_det':project_details,'mem':mem})

def MAN_proj_mangrs1(request,id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    project_details = project.objects.get(id=id) 
    return render(request,'MAN_proj_mangrs1.html',{'proj_det':project_details,'mem':mem})

def MAN_proj_mangrs2(request,id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    project_details = project.objects.get(id=id) 
    project_task = project_taskassign.objects.all()
    return render(request,'MAN_proj_mangrs2.html',{'proj_task':project_task,'proj_det':project_details,'mem':mem})

def MAN_daily_report(request,id): 
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    project_task = project_taskassign.objects.get(id=id)
    tester =tester_status.objects.all()
    return render(request,'MAN_daily_report.html',{'proj_task':project_task,'test':tester,'mem':mem})

def MAN_developers(request,id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    project_details = project.objects.get(id=id) 
    project_task = project_taskassign.objects.filter(tl_id = id)
    progress_bar= tester_status.objects.all()
    return render(request,'MAN_developers.html',{'proj_task':project_task,'proj_det':project_details,'prog_status':progress_bar,'mem':mem})


# completed projects- subeesh -manager module
  
def MAN_proj_cmpltd_new(request, id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    project_details=project.objects.filter(department=id)
    print (project_details.count())
    return render(request,'MAN_proj_cmpltd_show.html',{'project': project_details,'mem':mem})


def MAN_cmpltd_proj_det_new(request, id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    project_details = project.objects.get(id=id)

    return render(request,'MAN_cmpltd_proj_det_show.html',{'project': project_details,'mem':mem})

def MAN_proj_mngrs_new(request, id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    project_details = project.objects.get(id=id)
    return render(request,'MAN_proj_mngrs_show.html', {'project': project_details,'mem':mem})

def MAN_proj_mangrs1_new(request,id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    project_details = project.objects.get(id=id)
    return render(request,'MAN_proj_mangrs1_show.html', {'project': project_details,'mem':mem})

def MAN_proj_mangrs2_new(request, id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    project_details = project.objects.get(id=id)
    project_task = project_taskassign.objects.all()
    return render(request,'MAN_proj_mangrs2_show.html', {'project':project_details,'project_taskassign':project_task,'mem':mem})

def MAN_developers_new(request, id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    project_details = project.objects.get(id=id)
    project_task = project_taskassign.objects.filter(tl_id = id)
    progress_bar= tester_status.objects.all()
    return render(request,'MAN_developers_show.html', {'project':project_details,'project_taskassign':project_task,'prog_status':progress_bar,'mem':mem})

def MAN_daily_report_new(request, id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    project_task = project_taskassign.objects.get(id=id)
    tester = tester_status.objects.all()
    return render(request,'MAN_daily_report_show.html', {'project':project_task,'tester_status':tester,'mem':mem})

############## end ##########


#reported issue- akhil-admin mod

def BRadmin_Reportedissue_department(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id)
    departments=department.objects.all()
    return render(request, 'BRadmin_Reportedissue_department.html',{'department':departments,'Adm':Adm})

def BRadmin_Reportedissue(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id)
    departments=department.objects.get(id=id)
    designations=designation.objects.filter(department_id=departments)
    return render(request, 'BRadmin_Reportedissue.html',{'department':departments,'designation':designations,'Adm':Adm})

def BRadmin_ReportedissueShow(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id)
    designations=designation.objects.get(id=id)
    user=user_registration.objects.filter(designation=designations)
    departments=department.objects.filter()
    reported_issues=reported_issue.objects.all()
    return render(request,'BRadmin_ReportedissueShow.html',{'department':departments,'designation':designations,'reported_issue':reported_issues,'user_registration':user,'Adm':Adm})

def BRadmin_ReportedissueShow1(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id)
    reported_issues=reported_issue.objects.get(id=id)
    return render(request,'BRadmin_ReportedissueShow1.html',{'reported_issue':reported_issues,'Adm':Adm})


#reported issue- akhil-man mod

def MAN_Reportedissue_department(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    departments=department.objects.all()
    return render(request, 'MAN_Reportedissue_department.html',{'department':departments,'mem':mem})

def MAN_Reportedissue(request,id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    departments=department.objects.get(id=id)
    designations=designation.objects.filter(department_id=departments)
    return render(request, 'MAN_Reportedissue.html',{'department':departments,'designation':designations,'mem':mem})

def MAN_ReportedissueShow(request,id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    designations=designation.objects.get(id=id)
    user=user_registration.objects.filter(designation=designations)
    departments=department.objects.filter()
    reported_issues=reported_issue.objects.all()
    return render(request,'MAN_ReportedissueShow.html',{'department':departments,'designation':designations,'reported_issue':reported_issues,'user_registration':user,'mem':mem})

def MAN_ReportedissueShow1(request,id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    reported_issues=reported_issue.objects.get(id=id)
    return render(request,'MAN_ReportedissueShow1.html',{'reported_issue':reported_issues,'mem':mem}) 


############## end ##########


#task section-nimisha- man mod

def MAN_tasks(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    return render(request,'MAN_tasks.html',{'mem':mem})

def MAN_givetask(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    if request.method == 'POST':
        sc1 = request.POST['Department']
        sc2 = request.POST['designation']
        sc3 = request.POST['projectname']
        sc4 = request.POST['task']
        sc7 = request.POST['discrip']
        sc5 = request.POST['start']
        sc6 = request.POST['end']
        ogo = request.FILES['img[]']
        print(sc1,sc2)
        
        catry = task(tasks=sc4,files=ogo,description=sc7,
                                  startdate=sc5, enddate=sc6,department_id = sc1,designation_id = sc2,user_id = sc3)
        catry.save()
    dept = department.objects.all()
    desig = designation.objects.all()
    proj = project.objects.all()
    emp = user_registration.objects.all()
    return render(request,'BRadmin_givetask.html',{'desig':desig,'dept':dept,'project':proj,'emp':emp,'mem':mem})


def MAN_taskdesignation(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)   
    dept_id = request.GET.get('dept_id')
    Desig = designation.objects.filter(department_id=dept_id)
    print(Desig)
    return render(request, 'MAN_taskdesignation.html', {'Desig': Desig,'mem':mem})

def MAN_taskemployee(request):   
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    emp = user_registration.objects.filter(designation_id=desig_id)
    print(emp)
    return render(request, 'MAN_taskemployee.html', {'emp': emp,'mem':mem})

def MAN_currenttasks(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)  
    names =task.objects.filter(status='Progressing')
    return render(request,'MAN_currenttask.html',{'names': names,'mem':mem})

def MAN_previoustasks(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)  
    names =task.objects.filter(status='Completed')
    return render(request,'MAN_previoustasks.html',{'names': names,'mem':mem})


#task section-nimisha- admin mod

def BRadmin_tasks(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id)
    return render(request,'BRadmin_tasks.html',{'Adm':Adm})

def BRadmin_givetask(request):
    if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id)
    if request.method == 'POST':
        sc1 = request.POST['Department']
        sc2 = request.POST['designation']
        sc3 = request.POST['projectname']
        sc4 = request.POST['task']
        sc7 = request.POST['discrip']
        sc5 = request.POST['start']
        sc6 = request.POST['end']
        ogo = request.FILES['img[]']
        print(sc1,sc2)
        
        catry = task(tasks=sc4,files=ogo,description=sc7,
                                  startdate=sc5, enddate=sc6,department_id = sc1,designation_id = sc2,user_id = sc3)
        catry.save()
    dept = department.objects.all()
    desig = designation.objects.all()
    proj = project.objects.all()
    emp = user_registration.objects.all()
    return render(request,'BRadmin_givetask.html',{'desig':desig,'dept':dept,'project':proj,'emp':emp,'Adm':Adm})


def BRadmin_taskdesignation(request):  
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id) 
    dept_id = request.GET.get('dept_id')
    Desig = designation.objects.filter(department_id=dept_id)
    print(Desig)
    return render(request, 'BRadmin_taskdesignation.html', {'Desig': Desig,'Adm':Adm})

def BRadmin_taskemployee(request): 
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id)  
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    emp = user_registration.objects.filter(designation_id=desig_id)
    print(emp)
    return render(request, 'BRadmin_taskemployee.html', {'emp': emp,'Adm':Adm})


def BRadmin_currenttasks(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id)  
    names =task.objects.all()
    return render(request,'BRadmin_currenttask.html',{'names': names,'Adm':Adm})

def BRadmin_previoustasks(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id)  
    names =task.objects.all()
    return render(request,'BRadmin_previoustasks.html',{'names': names,'Adm':Adm})


############## end ##########

#upcoming projects -safdhar -admin mod


def BRadmin_upcoming(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id)
    return render(request,'BRadmin_upcomingprojects.html',{'Adm':Adm})

def BRadmin_viewprojectform(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    Adm = user_registration.objects.filter(id=Adm_id)
    if request.method == 'POST':
        sc1 = request.POST['Department']
        sc2 = request.POST['designation']
        sc3 = request.POST['projectname']
        sc4 = request.POST['discrip']
        sc5 = request.POST['start']
        sc6 = request.POST['end']
		
		
        progress=0
        catry = project_taskassign(project_id=sc3,
                                  description=sc4,
                                  startdate=sc5, enddate=sc6,extension='0')
        catry.save()
    dept = department.objects.all()
    desig = designation.objects.all()
    proj = project.objects.all()
    return render(request,'BRadmin_viewprojects.html',{'Adm':Adm,'desig':desig,'dept':dept,'project':proj})

def BRadmin_acceptedprojects(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    Adm = user_registration.objects.filter(id=Adm_id)
    pro =project.objects.filter(status='Accepted')
    return render(request,'BRadmin_acceptedprojects.html',{'Adm':Adm,'projects': pro})

def BRadmin_rejected(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    Adm = user_registration.objects.filter(id=Adm_id)
    pro =project.objects.filter(status='Rejected')
    return render(request,'BRadmin_rejectedprojectes.html',{'Adm':Adm,'projects': pro})

def BRadmin_createproject(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id)  
    if request.method == 'POST':
        sc1 = request.POST['Department']
        sc2 = request.POST['designation']
        sc3 = request.POST['projectname']
        sc4 = request.POST['discrip']
        sc5 = request.POST['start']
        sc6 = request.POST['end']
        ogo = request.FILES['img[]']
        print(sc5,sc6,ogo,sc1)
        progress=0
        catry = project(designation_id=sc2,department_id=sc1,project=sc3,
                                  description=sc4,
                                  startdate=sc5, enddate=sc6, files=ogo,progress=progress)
        catry.save()
    dept = department.objects.all()
    desig = designation.objects.all()	
    return render(request,'BRadmin_createproject.html',{'Adm':Adm,'dept':dept,'desig':desig})
   


def BRadmin_upcomingpro(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    Adm = user_registration.objects.filter(id=Adm_id)
    pro =project.objects.all()
    return render(request,'BRadmin_upcomingpro.html',{'Adm':Adm,'projects': pro})

def BRadmin_seradmintraineedesi1(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    Adm = user_registration.objects.filter(id=Adm_id)
    dept_id = request.GET.get('dept_id')
    Desig = designation.objects.filter(department_id=dept_id)
    print(Desig)
    return render(request, 'BRadmin_dropdown.html', {'Desig': Desig,'Adm':Adm})

def BRadmin_seradmindesig(request):
	print("safdhar")
	dept_id = request.GET.get('dept_id')
	Desig = designation.objects.filter(department_id=dept_id)
	print(Desig)
	return render(request, 'BRadmin_giveprojectdropdown.html', {'Desig': Desig})
def BRadmin_selectproject(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id)
    print("safdhar")
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    print(desig_id,dept_id)
    proj = project.objects.filter(department_id=dept_id)
    print(proj)
    return render(request, 'BRadmin_selectproject.html',{'project':proj,'Adm':Adm})


#upcoming projects -safdhar -man mod



def MAN_upcoming(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    return render(request,'MAN_upcomingprojects.html',{'mem':mem})
def MAN_viewprojectform(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    if request.method == 'POST':
        sc1 = request.POST['Department']
        sc2 = request.POST['designation']
        sc3 = request.POST['projectname']
        sc4 = request.POST['discrip']
        sc5 = request.POST['start']
        sc6 = request.POST['end']
        
        print(sc1,sc2)
        progress=0
        catry = project_taskassign(project_id=sc3,
                                  description=sc4,
                                  startdate=sc5, enddate=sc6,extension='0')
        catry.save()
    dept = department.objects.all()
    desig = designation.objects.all()
    proj = project.objects.all()
    return render(request,'MAN_viewprojects.html',{'desig':desig,'dept':dept,'project':proj,'mem':mem})

def MAN_acceptedprojects(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    pro = project.objects.filter(status='Accepted')
    return render(request,'MAN_acceptedprojects.html',{'projects':pro,'mem':mem})

def MAN_rejected(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    pro = project.objects.filter(status='Rejected')
    return render(request,'MAN_rejectedprojectes.html',{'projects':pro,'mem':mem})

def MAN_createproject(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    if request.method == 'POST':
        sc1 = request.POST['Department']
        sc2 = request.POST['designation']
        sc3 = request.POST['projectname']
        sc4 = request.POST['discrip']
        sc5 = request.POST['start']
        sc6 = request.POST['end']
        ogo = request.FILES['img[]']
        print(sc5,sc6,ogo,sc1)
        progress=0
        catry = project(designation_id=sc2,department_id=sc1,project=sc3,
                                  description=sc4,
                                  startdate=sc5, enddate=sc6, files=ogo,progress=progress)
        catry.save()
    dept = department.objects.all()
    desig = designation.objects.all() 
 
    return render(request,'MAN_createproject.html',{'desig':desig,'dept':dept,'mem':mem})

def MAN_upcomingprojectsview(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    pro =project.objects.all()
    return render(request,'MAN_upcomingprojectsview.html',{'projects': pro,'mem':mem})

def MAN_seradmintraineedesi1(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    dept_id = request.GET.get('dept_id')
    Desig = designation.objects.filter(department_id=dept_id)
    print('safdhar')
    return render(request, 'MAN_createprojectdropdown.html', {'Desig': Desig,'mem':mem})

def MAN_seradmindesig(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    print("safdhar")
    dept_id = request.GET.get('dept_id')
    Desig = designation.objects.filter(department_id=dept_id)
    print(Desig)
    return render(request, 'MAN_giveprojectdropdown.html', {'Desig': Desig,'mem':mem})
def MAN_selectproject(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    print("safdhar")
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    print(desig_id,dept_id)
    proj = project.objects.filter(department_id=dept_id)
    print(proj)
    return render(request, 'MAN_selectproject.html',{'project':proj,'mem':mem})

    
#*************************meenu**********************
def newdept(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id)
    condent = department.objects.all()
    return render(request,'BRadmin_Department.html',{'condent':condent,'Adm':Adm})

def add_dept(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id)
    return render(request,"BRadmin_add_dept.html",{'Adm':Adm})

def add_deptsave(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    Adm = user_registration.objects.filter(id=Adm_id)
    if request.method == 'POST':
        depart = request.POST['dept']
        a=department(department=depart)
        a.save()
        m="Successfully department added"
    return render(request,'BRadmin_add_dept.html',{'m':m,'Adm':Adm})


def delete(request, id):
    m = department.objects.get(id=id)
    m.delete()
    
    return redirect('/base_app/newdept')

def man_newdept(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    condent = department.objects.all()
    return render(request,'man_Department.html',{'condent':condent,'mem':mem})

def man_dept(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    return render(request,"man_add_dept.html",{'mem':mem})

def man_add_deptsave(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
 
    mem = user_registration.objects.filter(id=m_id)
    if request.method == 'POST':
        depart = request.POST['dept']
        a=department(department=depart)
        a.save()
        m="Successfully department added"
    return render(request,'man_add_dept.html',{'m':m,'mem':mem})


def man_delete(request, id):
    
    m = department.objects.get(id=id)
    m.delete()
    return redirect('/base_app/man_newdept')


############## end ##########
