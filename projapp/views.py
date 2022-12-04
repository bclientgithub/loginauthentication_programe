from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.template import RequestContext
from pkg_resources import empty_provider
from .models import Student
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
import random


def home(req):
    return render(req, 'home.html')


def ragistration(request):
    num = random.randrange(1121, 9899)
    global str_num
    str_num = str(num)
    return render(request, "ragistration.html", {"img": str_num})


def contact(req):
    return render(req, 'contact.html')


def login(req):
    return render(req, 'login.html')


def regTask(request):
    name = request.POST.get("name")
    fname = request.POST.get("fname")
    email = request.POST.get("email")
    password = request.POST.get("pass1")
    mob = request.POST.get("mob")
    dob = request.POST.get("dob")
    gender = request.POST.get("gender")
    from .models import Student
    ob = Student()
    ob.name = name
    ob.fname = fname
    ob.email = email
    ob.password = password
    ob.mob = mob
    ob.dob = dob
    ob.gender = gender
    cap = request.POST.get("captha")
    if str(cap) == str_num:
       
        # return redirect('/ragistration')
        subject = "welcome to GFG world:"
        message = "Hithank you for registering in geeksforgeeks."
        email_from = 'akashsharmaBclient@gmail.com'
        recipient_list = request.POST.get("email")
        send_mail(subject, message, email_from, [recipient_list])
        ob.save()
        return HttpResponse("<h4>YOUR FORM HAS BENN SUBMITED SUCCESSFULLY..........</h4>")
    else:
        return HttpResponse("<h3>YOU FILL THE WRONG CAPTCHA........... </h3>")
    # return redirect('/ragistration')


def loginTask(request):
    global email
    global password
    role = request.POST.get("Login")
    if role == "Student":
        email = request.POST.get("email")
        password = request.POST.get("password")
        from .models import Student
        db = Student.objects.all()
        for i in db:
            # if role==i.role:
            if email == i.email:
                if password == i.password:
                    return redirect("/student")
            if email != i.email and password == i.password:
                return HttpResponse("please insert correct email")
            if email == i.email and password != i.password:
                return HttpResponse("please insert correct email")

    elif role == "Faculty":
        email = request.POST.get("email")
        password = request.POST.get("password")
        from .models import Faculty
        db = Faculty.objects.all()
        for i in db:
            if role == "Faculty":
                if email == i.email:
                    if password == i.password:
                        return redirect("/faculty")
    elif role == "Admin":
        email = request.POST.get("email")
        password = request.POST.get("password")
        from .models import Faculty, Student
        db = Student.objects.all()
        st = Faculty.objects.all()

        return render(request, 'admin.html', {'db': db})


#         for i in db:
#             if email == i.email:
#                 if password == i.password:
#                     return redirect("/admin")


# def admin(req):
#     from .models import Student
#     res = Student.objects.filter(email=email)
#     return render(req, 'admin.html', {'res': res})


def student(req):
    from .models import Student
    rec = Student.objects.filter(email=email)
    return render(req, 'student.html', {'rec': rec})


def facultytask(req):

    name = req.GET.get("name")
    fname = req.GET.get("fname")
    email = req.GET.get("email")
    password = req.GET.get("pass1")
    mob = req.GET.get("mob")
    dob = req.GET.get("dob")
    gender = req.GET.get("gender")
    from .models import Faculty

    ob = Faculty()
    ob.name = name
    ob.fname = fname
    ob.email = email
    ob.password = password
    ob.mob = mob
    ob.dob = dob
    ob.gender = gender
    ob.save()
    return redirect('/')


def ragistration2(req):
    return render(req, 'ragistration2.html')


def faculty(req):
    from .models import Faculty
    rec = Faculty.objects.filter(email=email)
    return render(req, 'faculty.html', {'rec': rec})
    # from projapp.models import Faculty
    # rec=Faculty.objects.filter(email=email)
    # return render(req,'student.html',{'rec':rec})


def delete(req):
    eid = req.GET.get('eid')
    obj = Student.objects.get(id=eid)
    obj.delete()
    return redirect("/student")
def forget(req):
    return render(req,'forget.html')
def forgettask(request):
    # num = random.randrange(1121, 9899)
    # str_num = str(num)
    
    recipient_list=request.POST.get('email')
    subject = "welcome to GFG world:"
    message = "Hithank you for registering in geeksforgeeks."
    email_from = 'akashsharmaBclient@gmail.com'
    send_mail(subject, message, email_from, [recipient_list])
    return redirect('/forget')



def update(req):
    update = req.GET.get('update')
    emp = Student.objects.filter(id=update)

    if req.method == "GET":

        return render(req, 'update.html', {'emp': emp})
    else:
        obj = Student()
        obj.name = req.POST.get('name')
        obj.fname = req.POST.get('fname')
        obj.email = req.POST.get('email')
        obj.password = req.POST.get('password')
        obj.mob = req.POST.get('mob')
        obj.dob = req.POST.get('dob')
        obj.gender = req.POST.get('gender')
        obj.save()
        return redirect('/student')


# Create your views here.
