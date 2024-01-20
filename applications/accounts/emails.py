# from django.core.mail import send_mail
# import random
# from django.conf import settings
# from .models import User
#
#
# def send_otp(email):
#     subject = f'Your verification email - {email}'
#     otp = random.randint(100000, 999999)
#     message = f'your otp is {otp}'
#     email_from = settings.EMAIL_HOST_USER
#     send_mail(subject, message, email_from, [email])
#     user = User.objects.get(email=email)
#     user.token = otp
#     user.save()
