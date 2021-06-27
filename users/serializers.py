from rest_framework import serializers
from dj_rest_auth.serializers import LoginSerializer
from django.contrib.auth import authenticate


class TwoFASerializer(LoginSerializer):
    verification_code = serializers.IntegerField(required=False, allow_null=True)

    
