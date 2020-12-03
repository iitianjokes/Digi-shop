from django.views import View
from django.shortcuts import render , redirect , HttpResponse
from django.contrib.auth.hashers import check_password
from shop.models import User
from shop.utils.email_sender import sendEmail
import random
import math

def SendOtp(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    otp = math.floor(random.random()*10000)
    html = f'''
        <h4>Hello {name}</h4>
        <p>Your Verification Code <b> {otp} <b></p>
        <br>
        Thanku
     '''
    print(name , email)
    if name and email:
        response = sendEmail(name = name , email=email , htmlcontent=html , subject= "verify your email")


        try:
            if (response.json()['messageId']):
                request.session['verification-code'] = otp
                return HttpResponse("{'message': 'success'}", status=200)
            else:
                return HttpResponse(status=400)
        except:
            return HttpResponse(status=400)

def verifycode(request):
    code = request.POST.get('code')
    otp = request.session.get('verification-code')
    print(code , otp)
    if(str(otp) == code):
        return HttpResponse("{'Message' : 'Sucess'}" , status=200)

    else:
        return  HttpResponse(status=400)