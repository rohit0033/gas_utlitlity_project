from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from service_requests.models import ServiceRequest
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate
from .models import SupportRep
from django.views.decorators.csrf import csrf_exempt
import base64

def is_support_rep(user):
    try:
        SupportRep.objects.get(user=user)
        return True
    except SupportRep.DoesNotExist:
        return False

def update_request_status(request, pk):
    if 'HTTP_AUTHORIZATION' in request.META:
        auth_header = request.META['HTTP_AUTHORIZATION']
        try:
            auth_type, encoded_credentials = auth_header.split(' ')
            if auth_type.lower() == 'basic':
                username, password = base64.b64decode(encoded_credentials).decode().split(':')
                user = authenticate(request, username=username, password=password)
                if user is not None and is_support_rep(user):
                    service_request = get_object_or_404(ServiceRequest, pk=pk)
                    if request.method == 'POST':
                        new_status = request.POST.get('status')
                        if new_status in [choice[0] for choice in ServiceRequest.STATUS_CHOICES]:
                            service_request.status = new_status
                            service_request.save()
                            return JsonResponse({'message': 'Status updated successfully', 'status': new_status})
                        else:
                            return JsonResponse({'error': 'Invalid status provided'}, status=400)
                    else:
                        return JsonResponse({'error': 'Invalid request method'}, status=405)
                else:
                    return JsonResponse({'error': 'Invalid credentials or not a support rep'}, status=401)
        except Exception as e:
            print(f"Authentication error: {e}")
            return JsonResponse({'error': 'Invalid authentication header'}, status=400)
    response = HttpResponse(status=401)
    response['WWW-Authenticate'] = 'Basic realm="api"'
    return response