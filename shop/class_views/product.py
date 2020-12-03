from django.views import View
from django.shortcuts import render , redirect , HttpResponse
from django.contrib.auth.hashers import check_password
from shop.models import User ,Product , ProductImage ,Payment
from django.db.models import Q

def productDetails(request , product_id):
    product = Product.objects.get(id=product_id)
    images = ProductImage.objects.filter(product = product.id)
    download_url = False
    try:
        session_user = request.session.get('user')
        if session_user:
            user_id = session_user.get('id')
            user = User(id=user_id)
            payment = Payment.objects.filter(~Q(status = "Failed"),product = product , user = user)
            if len(payment) !=0:
                download_url = True

    except:
        pass;
    return render( request,'product_detail.html',{'product' : product , 'images': images , 'download_url': download_url})

