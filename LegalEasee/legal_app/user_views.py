from django.shortcuts import render,HttpResponse,redirect
from .models import Feedback,User,Advisor
from django.contrib import messages


def user_reg(request):
     return render(request,'legal_app/html/user/user_reg.html')
   
def user_login(request):
    if(request.method=="GET"):
        return render(request,'legal_app/html/user/user_login.html')
    if(request.method=="POST"):
        user_email=request.POST["email"]
        user_password=request.POST["password"]
        user_list=User.objects.filter(email=user_email,password=user_password)
        if len(user_list)>0:
            request.session["user_key"]=user_email
            # request.session["user_role"]="user"
            return redirect("user_home")
        else:
            messages.error(request,"Invalid Credentials🥴")
            return redirect("user_login")

def user_home(request):
    if(request.method=="GET"):
        # fetch/get the value from session
        user_email=request.session["user_key"]
        user_obj=User.objects.get(email=user_email)
        # Sending object from view to template
        # Create a dictionary and bind object with a key and then send the dictionary
        user_dict={"user_info":user_obj}
        return render(request,'legal_app/html/user/user_home.html', user_dict)

def user_feedback(request):
    if(request.method=="GET"): #http protocol method
        user_email=request.session["user_key"] # getting email from session
        user_obj=User.objects.get(email=user_email) #get user data from his email
        user_dict={"user_info":user_obj} #get user data stored in dictionary
        return render(request,'legal_app/html/user/user_feedback.html',user_dict)
    if(request.method=="POST"):
        user_email=request.POST["email"]
        user_name=request.POST["name"] #it will read data from textbox
        user_remark=request.POST["remark"]
        user_rating=request.POST["rating"]
        user_pic=request.POST["pic_path"]
        feedback_obj=Feedback(email=user_email,name=user_name,remark=user_remark,rating=user_rating,user_pic=user_pic)
        feedback_obj.save()
        messages.success(request,"Thanyou for your Feedback!😊")
        # return render(request,'legal_app/html/user/user_feedback.html')
        return redirect("user_feedback")
    
def user_reg(request):
    if(request.method=="GET"): #http protocol method
        return render(request,'legal_app/html/user/user_reg.html')
    if(request.method=="POST"):
        user_name=request.POST["name"] #it will read data from textbox
        user_email=request.POST["email"]
        user_password=request.POST["password"]
        phone_no=request.POST["phone"]
        user_pic=request.FILES.get("profile_pic")
        user_obj=User(name=user_name,email=user_email,password=user_password,phone=phone_no,pic_name=user_pic)
        user_obj.save()
        return redirect("user_login")
    
def user_logout(request):
    request.session.flush()
    messages.success(request,"Successfuly Logged out, Thank you")
    return redirect("user_login")

def advisors(request):
    advisors_list=Advisor.objects.all()
    # will returns list of feedback table objects
    advisors_dict={"advisors_key":advisors_list}
    return render(request,"legal_app/html/user/advisors.html",advisors_dict)
