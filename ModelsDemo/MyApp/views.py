from django.shortcuts import render
from .models import Course
from django.http import  HttpResponse

def addCourse(request):
    if request.method=="GET":
        return render(request,"addCourse.html",{})
    else:
        cname=request.POST["cname"]
        duration=request.POST["duration"]
        fees_details=request.POST["fees_details"]
        c1=Course(cname=cname,duration=duration,fees_details=fees_details)
        c1.save()
        return HttpResponse("Record Added")

    
