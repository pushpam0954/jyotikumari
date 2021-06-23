from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

from django.core.mail import send_mail

from django.conf import settings


def Home(request):
    if request.method == "POST":
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        message = request.POST['message']

        # send the email
        send_mail(
            'message_from_' + message_name,  # subject
            "message is = " + message  + "\nMessage from = " + message_email,
            # message
            message_email,  # form email
            ['pushpam0954@gmail.com', ],  # to email
            fail_silently=False

        )

        return render(request, 'Home.html')
    else:
        return render(request, 'Home.html')