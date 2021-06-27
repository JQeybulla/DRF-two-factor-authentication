from django.shortcuts import render
from dj_rest_auth.views import LoginView
from .models import CustomUser
from django.shortcuts import get_object_or_404
from random import randint
from django.core.mail import send_mail
from rest_framework.response import Response
from .serializers import TwoFASerializer
from rest_framework import status
from django.utils import timezone
from datetime import timedelta
from rest_framework.views import APIView
# from rest_framework import generics


# Create your views here.

class CustomLoginView(LoginView):

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data)
        self.serializer.is_valid(raise_exception=True)

        username = self.serializer.data['username']
        user = get_object_or_404(CustomUser, username=username)

        if user.two_factor_auth_status:
            email = user.email

            random_code = randint(1111, 9999)
            msg = "Your verification code: " + str(random_code)

            user.two_factor_code = random_code
            user.tfa_code_reset = timezone.now()
            user.save()

            send_mail(
                'Two Factor Authentication code',
                msg,
                'from@example.com',
                [email],
                fail_silently=False,
            )
            return Response("Two fCator authentiation code sent to your email address")

        self.login()
        return self.get_response()

        

class TwoFactorAuth(LoginView):

    serializer_class = TwoFASerializer

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data)
        self.serializer.is_valid(raise_exception=True)

        username = self.serializer.data['username']
        user = get_object_or_404(CustomUser, username=username)
        code = self.serializer.data['verification_code']

        if code == user.two_factor_code:
            if timezone.now() - user.tfa_code_reset < timedelta(minutes=1):
                self.login()
                user.two_factor_code = None
                user.save()
                return self.get_response()
            return Response({'message':'This code has expired'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response({'message':'Verification code is incorrect'}, status=status.HTTP_406_NOT_ACCEPTABLE)



class TwoFactorAuthStatus(APIView):
    """
    POST request turns 'two FA' on if it is off and vice versa 
    """
    def post(self, request, *args, **kwargs):
        user = self.request.user
        if user.two_factor_auth_status:
            user.two_factor_auth_status = False
            user.save()
            return Response("Two Factor authentication turned off")
        user.two_factor_auth_status = True
        user.save()
        return Response("Two Factor authentication turned on")