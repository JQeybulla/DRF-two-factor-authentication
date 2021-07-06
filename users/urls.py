from django.urls import path
from .views import TwoFactorAuthStatus

urlpatterns = [
    path('two-fa-status/', TwoFactorAuthStatus.as_view(), name='twofa_status'),
]