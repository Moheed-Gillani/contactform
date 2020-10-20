from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from Emailsending.settings import EMAIL_HOST_USER
def index(request):
    return render(request,'home/index.html')
def mailing(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        subject="This is from Email : "+str(email)
        send_mail(subject,message,EMAIL_HOST_USER,[EMAIL_HOST_USER],fail_silently=False)
        return render(request,'home/success.html',{'email':email,'Name':name})
    return render(request,'home/index.html')