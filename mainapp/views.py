from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views import View
import requests
from django.contrib.auth.models import User
from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes, permission_classes

from rest_framework import status
from rest_framework import viewsets
from .serializers import *
from .models import *

# GIU views
def login_view(request):
    if request.method == 'POST' and request.POST.get('forma')=='f1':
        user = authenticate(
            username = request.POST.get('username'),
            password = request.POST.get('password')
        )
        if user is None:
            return redirect("/login/")
        login(request, user)
        return redirect('/')
    elif request.method == 'POST' and request.POST.get('forma')=='f2':
        try:
            User.objects.create_user(
                username=request.POST.get('username'),
                email=request.POST.get('email'),
                password=request.POST.get('password')
            )
        finally:
            return redirect('/login/')
    return render(request, 'login_form.html')

def logoutView(request):
    logout(request)
    return redirect('/login')

def home(request):
    user = None
    if request.user.is_authenticated:
        user = request.user
    context = {
        'user' : user
    }
    return render(request, 'index.html', context)

def profile(request):
    if request.user.is_authenticated:
        user = Profile.objects.get(user_id=request.user)
        context = {
            "user" : user
        }
        return render(request, 'profile.html', context)
    return redirect('/login/')


def list_of_scenario(request):
    if request.user.is_authenticated:
        context = {
            "keys" : Keywords.objects.all()
        }
        return render(request, 'prompts.html', context)
    return redirect('/login/')


# API views
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class GetAnswersView(View):
    def get(self, request, *args, **kwargs):
        # Assuming the key is passed in the request headers
        key = request.headers.get('key')  # Replace 'Your-Key-Header' with the actual header key

        if not key:
            return JsonResponse({'error': 'Key not provided in headers'}, status=400)

        # Assuming the token is passed in the request headers
        token = request.headers.get('Authorization').split(' ')[1]  # Replace 'Authorization' with the actual header key for token

        if not token:
            return JsonResponse({'error': 'Token not provided in headers'}, status=400)

        try:
            # Validate the token and retrieve the user
            user = Token.objects.get(key=token).user

            # Retrieve the Keywords instance associated with the user
            keyword = Keywords.objects.get(user_id=user)

            # Retrieve answers associated with the keyword
            answers = Answers.objects.filter(key_id=keyword)

            # Serialize the answers data as needed
            serialized_answers = [{'answer_text': answer.answer_text, 'audio_link': answer.audio_link} for answer in answers]

            return JsonResponse({'answers': serialized_answers}, status=200)

        except:
            return JsonResponse({'error': "An exception occurred"}, status=400)
        # except Token.DoesNotExist:
        #     return JsonResponse({'error': 'Invalid token'}, status=401)
        #
        # except User.DoesNotExist:  # Catch the User.DoesNotExist exception
        #     return JsonResponse({'error': 'Invalid key'}, status=400)
        #
        # except Keywords.DoesNotExist:
        #     return JsonResponse({'error': 'No keyword associated with the provided key'}, status=404)