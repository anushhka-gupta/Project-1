from django.shortcuts import render,HttpResponse,redirect
from .models import Contact,Feedback,Service
from django.contrib import messages

def all_feedback(request):
    feedback_list=Feedback.objects.all()
    # will returns list of feedback table objects
    feedback_dict={"feedback_key":feedback_list}
    return render(request,"legal_app/html/all_feedback.html",feedback_dict)

# Create your views here.
def home(request):
    # return HttpResponse("<h1>This is Home Page</h1>")
    return render(request,'legal_app/html/index.html')

def about_us(request):
    return render(request,'legal_app/html/aboutus.html')

def contact_us(request):
    if(request.method=="GET"): #http protocol method
        return render(request,'legal_app/html/contactus.html')
    if(request.method=="POST"):
        user_name=request.POST["name"]
        user_email=request.POST["email"] #it will read data from textbox
        phone_no=request.POST["phone"]
        query=request.POST["question"]

        feedback_obj=Contact(email=user_email,name=user_name,phone=phone_no,question=query)
        feedback_obj.save()
        messages.success(request,"Thanyou for Contacting Us!😊")
        return redirect("contact_us")

def services(request):
    services_list=Service.objects.all()
    # will returns list of feedback table objects
    services_dict={"services_key":services_list}
    return render(request,"legal_app/html/services.html",services_dict)
