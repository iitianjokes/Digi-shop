from django.shortcuts import render , redirect

def after_login(get_response):

    def middleware(request):
        user = request.session.get('user')
        if user:
            return redirect('home')
        else:
            return get_response(request)
    return middleware