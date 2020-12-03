from django.views import View
from django.shortcuts import render , redirect
from django.contrib.auth.hashers import check_password
from shop.models import User


class loginView(View):
    return_url = None
    def get(self, request):
        loginView.return_url = request.GET.get('return_url')
        return render(request, 'login.html')


    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            flag = check_password(password=password, encoded=user.password)
            if flag:
                temp = {}
                temp['email'] = user.email
                temp['id'] = user.id
                request.session['user'] = temp
                if loginView.return_url:
                    return redirect(loginView.return_url)
                return redirect('home')
            else:
                return render(request, 'login.html', {'err': "Email Or Password Invalid"})
        except:
            return render(request, 'login.html', {'err': "Email Or Password Invalid"})
