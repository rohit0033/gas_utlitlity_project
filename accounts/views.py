from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser  # Import your CustomUser model
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt # Import csrf_exempt
from django.middleware.csrf import get_token
import json  # Import the json module


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('address', 'phone_number')  # Include any additional fields from CustomUser

@csrf_exempt # Add csrf_exempt decorator
def register_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parse JSON data from the request body
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        form = CustomUserCreationForm(data)  # Pass the parsed data to the form
        if form.is_valid():
            user = form.save()
            login(request, user)
            return JsonResponse({'message': 'Registration successful', 'username': user.username}, status=201)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

import base64
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Generate Basic Auth string
            message = f"{username}:{password}"
            encoded_bytes = base64.b64encode(message.encode('utf-8'))
            encoded_string = encoded_bytes.decode('utf-8')
            return JsonResponse({
                'message': 'Login successful',
                'username': username,
                'basic_auth_string': f"Basic {encoded_string}"  # Include "Basic " prefix
            }, status=200)
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
@csrf_exempt # Add csrf_exempt decorator
def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'Logout successful'}, status=200)