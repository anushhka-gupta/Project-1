from django.shortcuts import render,HttpResponse,redirect
from .models import Advisor
from django.contrib import messages

def advisor_login(request):
    if(request.method=="GET"):
        return render(request,'legal_app/html/advisor/advisor_login.html')
    if(request.method=="POST"):
        advisor_email=request.POST["email"]
        advisor_password=request.POST["password"]
        advisor_list=Advisor.objects.filter(email=advisor_email,password=advisor_password)
        if len(advisor_list)>0:
            request.session["advisor_key"]=advisor_email
            # request.session["advisor_role"]="advisor"
            return redirect("user_home")
        else:
            messages.error(request,"Invalid Credentials🥴")
            return redirect("advisor_login")