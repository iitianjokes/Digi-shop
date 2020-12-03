
from django.views import View
from django.shortcuts import render , redirect
from django.contrib.auth.hashers import check_password ,make_password
from shop.models import User

class signupView(View):

    def get(self , request):
        return render(request, 'signup.html')


    def post(self , request):

        try:
            name = request.POST.get('name')
            mobileno = request.POST.get('mobileno')
            email = request.POST.get('email')
            password = request.POST.get('password')
            haspass = make_password(password=password)
            user = User(name=name, mobileno=mobileno, email=email, password=haspass)
            result = user.save()
            return render(request, 'login.html')

        except:

            return render(request, 'signup.html', {'err': "User is Already Register"})



