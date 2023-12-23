from django.shortcuts import render,redirect
from career_map.models import persion_detail,post_job,jobs
from career_map.forms import persion_detailForm,post_jobForm,jobsForm
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail,EmailMessage



# Create your views here.
def show(request):
    data=persion_detail.objects.all()
    return render(request,'show.html',{'data':data})
def log(request):
    return render(request,'logins.html')
def ret(request):
    s=persion_detail.objects.all()
    return render(request,'display.html',{'s':s})
def su(request):
    name=request.POST['user_name']
    password=request.POST['password']
    info=persion_detail.objects.all()
    temp=0
    for i in info:
        if i.user_name==name and i.password==password:
            temp=1
            break
    if temp==1:
        return render(request, 'success.html', {'name': name})
    else:
        return render(request,'one.html')
def add(request):
    fo=persion_detailForm()
    if request.method=="POST":
        s=persion_detailForm(request.POST,request.FILES)
        if s.is_valid():
            s.save()
            return redirect('/log')
    return render(request,'registaion.html',{'fo':fo})
def reset_password(request):
    return render(request,'reset_password.html')
def check(request):
    name=request.POST['user_name']
    mail=request.POST['mail_id']
    details=persion_detail.objects.all()

    for i in details:
        if i.user_name==name and i.mail_id==mail:
            return render(request,'reset.html',{'d':i})


def change(request):
    d=persion_detail.objects.get(id=id)

    if request.method=='POST':
        f=persion_detailForm(request.POST,request.FILES,instance=d)
        if f.is_valid():
            f.save()

            return redirect('/log')
    return render(request,'change.html',{'d':d})

def go_to_login(request):
    return redirect('/log')
def add_details(requst):
    return redirect('/add')
def about_us(request):
    return render(request,'about.html')
def home(request):
    return render(request,'success.html')
def post_jobs(request):##################################
    return render(request,'post_jobs.html')
def poster(request):
    name = request.POST['user_name']
    password = request.POST['password']
    lop = post_job.objects.all()
    temp = 0
    for i in lop:
        if i.user_name == name and i.password == password:
            temp = 1
            break
    if temp == 1:
        return render(request, 'info.html', {'name': name})
    else:
        return redirect('/post_jobs')
def register_the_recruter(request):
    fo = post_jobForm
    if request.method == "POST":
        s = post_jobForm(request.POST)
        if s.is_valid():
            s.save()
            return redirect('/post_job')
    return render(request, 'register_the_recruter.html', {'fo': fo})
def search(request):
    g=request.POST['job_title']
    if g=="ALL":
        y=jobs.objects.all()
    else:
        y=[]
        k=0
        l=jobs.objects.all()
        for i in l:
            if i.job_title==g:
                y.append(i)
                k+=1
        if k==0:
            return HttpResponse("details not found")

    return render(request,'job.html',{'j':y})

def recruter_forgot_password(request):
    return render(request,'get_recruter_details.html')
def check_recrutor(request):
    name = request.POST['user_name']
    mail = request.POST['mail_id']
    details = post_job.objects.all()

    for i in details:
        if i.user_name == name and i.mail_id == mail:
            return render(request, 'reset_recrutor_password.html', {'d': i})

def change_recrutor_password(request):
    d = post_job.objects.get(id=id)

    if request.method == 'POST':
        f = post_jobForm(request.POST, instance=d)
        if f.is_valid():
            f.save()
            return redirect('/post')
    return render(request, 'change_recrutor_password.html', {'d': d})

def info(request):
    domain=request.POST['domain']
    if domain=="ALL":
        g=persion_detail.objects.all()
    else:
        g=[]
        c=0
        k=persion_detail.objects.all()
        for i in k:
            if i.domain==domain:
                g.append(i)
                c+=1
        if c==0:
            return HttpResponse("details not found")

    return render(request,'info_details.html',{'g':g})

def new_post(request):

    y=jobs.objects.all()
    return render(request,'new_post.html',{'y':y})
def add_job(request):
    h=jobsForm()
    if request.method=="POST":
        f=jobsForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/new_post')
    return render(request,'add_job.html',{'h':h})

def contact_details(request):
    return render(request,'contact_details.html')
def service(request):
    return render(request,'service.html')
def conditions(request):
    return render(request,'conditions.html')
def logins(request):
    return render(request,'logins.html')

def apply(request):
    return render(request,'emails.html')

def emails(request):
    mail=post_job.objects.all()
    if request.method=='POST':
        messag = request.POST['message']
        send_mail('contact Form',
                  messag,
                  settings.EMAIL_HOST_USER,
                  ['kaviyanagaraj42@gmail.com'],
                  fail_silently=False)
        EmailMessage.attach_file('')
    return render(request,'emails.html')





