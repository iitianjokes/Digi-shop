from django.shortcuts import render , redirect
from shop.models import Product ,User , Payment
from e_learn.settings import PAYMENT_API_AUTH ,PAYMENT_API_KEY
from instamojo_wrapper import Instamojo
API = Instamojo(api_key=PAYMENT_API_KEY,
                    auth_token=PAYMENT_API_AUTH,endpoint='https://test.instamojo.com/api/1.1/')

import math



def createpayment(request , product_id):

    user = request.session.get('user')
    product = Product.objects.get(id = product_id)
    userObject = User.objects.get(id = user.get('id'))
    amount = (product.price -(product.price * (product.discount/100)))

    response = API.payment_request_create(
        amount=math.floor(amount),
        purpose=f'Payment For {product.name}',
        send_email=True,
        email= user.get('email'),
        phone= userObject.mobileno,
        buyer_name= userObject.name,
        redirect_url="http://localhost:8000/complete-payment/"

    )

    print ("res:",response)
    payment_request_id = response['payment_request']['id']
    payment = Payment(user = User(id = user.get('id')) , product = product , payment_request_id = payment_request_id )
    payment.save()
    url = response['payment_request']['longurl']
    print(url)
    return redirect(url)


def verifypayment(request):
    payment_id = request.GET.get("payment_id")
    payment_request_id = request.GET.get('payment_request_id')
    response = API.payment_request_payment_status(payment_request_id, payment_id)
    status = response['payment_request']['payment']['status']
    if status is not 'Failed':
        payment = Payment.objects.get(payment_request_id=payment_request_id)
        payment.payment_id=response['payment_request']['payment']['payment_id']
        payment.status = status
        payment.save()
        return render(request , "download_product_after_payment.html" , {"payment": payment})
    else:
        return redirect('home')


