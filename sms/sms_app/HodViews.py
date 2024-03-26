
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from sms_app.models import CustomUser, Staff, Grade, Cname
from django.contrib import messages
from django.urls import reverse


def admin_home(request):
    return render(request, "hod_template/home_content.html")


def add_staff(request):
    return render(request, "hod_template/add_staff_template.html")


def add_staff_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        address=request.POST.get("address")
        
        try:
            user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=2 )
            user.staff.address=address
            user.save()
            messages.success(request,"Successfully Added Staff")
            return HttpResponseRedirect("add_staff")
        except Exception as e:
            messages.error(request, f"Failed to Add Staff: {str(e)}")
            return HttpResponseRedirect("add_staff")

def add_grade(request):
    return render(request, "hod_template/add_grade_template.html")


def add_grade_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        grade=request.POST.get("grade")
        try:
            grade_model=Grade(grade_name=grade)
            grade_model.save()
            messages.success(request,"Successfully Added Grade")
            return HttpResponseRedirect("add_grade")
        except Exception as e:
            messages.error(request, f"Failed To Add Grade: {str(e)}")
            return HttpResponseRedirect("add_grade")

def add_class(request):
    return render(request, "hod_template/add_class_template.html")


def add_class_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        class_name=request.POST.get("Cname")
        try:
            class_model=Cname(class_name=class_name)
            class_model.save()
            messages.success(request,"Successfully Added Class")
            return HttpResponseRedirect("add_class")
        except Exception as e:
            messages.error(request, f"Failed To Add Class: {str(e)}")
            return HttpResponseRedirect("add_class")


def add_student(request):
   grades=Grade.objects.all()
   classes=Cname.objects.all()
   return render(request, "hod_template/add_student_template.html", {"grades":grades ,"classes":classes} ) 


def add_student_save(request):
     if request.method!="POST":
        return HttpResponse("Method Not Allowed")
     else:
        name=request.POST.get("name")
        school_attended=request.POST.get("school_attended")
        grade_attended=request.POST.get("grade_attended")
        email=request.POST.get("email")
        password=request.POST.get("password")
        address=request.POST.get("address")
        try:
            user=CustomUser.objects.create_user(name=name,password=password,email=email,last_name=last_name,first_name=first_name,user_type=2 )
            user.staff.address=address
            user.save()
            messages.success(request,"Successfully Added Staff")
            return HttpResponseRedirect("add_staff")
        except Exception as e:
            messages.error(request, f"Failed to Add Staff: {str(e)}")
            return HttpResponseRedirect("add_staff")

     