from django.views import View
from django.shortcuts import render , redirect ,HttpResponse
from django.contrib.auth.hashers import check_password , make_password
from shop.models import User
from shop.utils.email_sender import sendEmail
import math
import random


class ResetPassword(View):
    def get(self , request):
        return render(request , 'reset-password.html' , {'form1': True})


    def post(self, request):
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        error = None;
        if len(password)<6:
            error = 'Password Must be More Than 6 Character'
        elif len(repassword)<6:
            error = 'Re-Password Must be More Than 6 Character'
        elif password != repassword:
            error = 'Password Not Match'

        if error :
           return render(request, 'reset-password.html', {'form3': True , 'error' : error})

        else:
            email =   request.session.get('reset-password-email')
            user = User.objects.get(email = email)
            user.password = make_password(password)
            user.save()
            request.session.clear()
            sendEmailchange(user)
            return render(request , 'login.html' , {'message' : 'Password Changed Succesful'})

def sendEmailchange(user):
    html = " <b>You Password Has Changed Successfully<b>"
    sendEmail(user.name , user.email ,'Password Changed' , htmlcontent=html)

def verifyResetPasswordCode(request):
    code = request.POST.get('code')
    sessiocode = request.session['reset-password-verification-code']
    if code == str(sessiocode):
        return render(request , 'reset-password.html' , {'form3' : True})

    else:
        return render(request, 'reset-password.html', {'form3': True})


class PasswordResetVerification(View):
    def post(self, request):
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            otp = math.floor(random.random() * 10000)
            html = f'''

                    <h4>Your Password Reset Verification Code {otp}</h4>
            
                    '''
            sendEmail("User", email , "Reset Verification Code" , html)
            request.session['reset-password-verification-code'] = otp
            request.session['reset-password-email'] = email
            return render(request, 'reset-password.html', {'form2' : True})

        except:

            return redirect('reset-password')

