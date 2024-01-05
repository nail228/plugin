from django.shortcuts import render

from .models import Users

import datetime
from rest_framework.response import Response

from rest_framework.decorators import api_view
from django.views.decorators.http import require_http_methods
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView


@api_view(['POST'])
@require_http_methods(["POST"])

def login(request):
    if request.method=='POST':
        return Response(request.body)
def logout(request):
    pass

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter