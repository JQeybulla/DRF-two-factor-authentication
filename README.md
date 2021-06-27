# DRF-two-factor-authentication

Simple project in Django Rest Framework with Sign up and Log in features. Two factor authentication is provided. User can turn on and off twoFA.
If twoFA is turned on and user tries to log in an email will be sent to user with 4 digit verification code(at the moment the EMAIL_BACKEND is 
'django.core.mail.backends.console.EmailBackend' so email will be shown in console only. Can be replaced with real email server in real project)
If user enters the verification code within one minute (can be changed) the user is logged in. In any other case a failure message is returned.


django allauth and dj-rest-auth are used for authentication

https://django-allauth.readthedocs.io/en/latest/installation.html

https://dj-rest-auth.readthedocs.io/en/latest/index.html
