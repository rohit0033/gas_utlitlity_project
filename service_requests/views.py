from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm
from django.http import JsonResponse
from django.core.serializers import serialize
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.csrf import csrf_exempt
import json


def is_authenticated(user):
    return user.is_authenticated


@csrf_exempt
@user_passes_test(is_authenticated, login_url=None)
def create_service_request(request):
    # Ensure authentication
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Authentication required'}, status=401)

    # Handle POST requests
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        form = ServiceRequestForm(data)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            return JsonResponse({'message': 'Service request created successfully'}, status=201)
        else:
            # Form is invalid, return errors
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        # Handle non-POST requests
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def service_request_list(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Authentication required'}, status=401)
    service_requests = ServiceRequest.objects.filter(user=request.user)
    # Manually construct the JSON response
    service_request_list = []
    for service_request in service_requests:
        service_request_list.append({
            'id': service_request.pk,
            'category': service_request.category,
            'description': service_request.description,
            'status': service_request.status,
            'created_at': service_request.created_at.isoformat(),  # Format datetime
        })
    return JsonResponse(service_request_list, safe=False)


@csrf_exempt
def service_request_detail(request, pk):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Authentication required'}, status=401)
    try:
        service_request = ServiceRequest.objects.get(pk=pk, user=request.user)
        service_request_json = serialize('json', [service_request])
        return JsonResponse(service_request_json, safe=False)
    except ServiceRequest.DoesNotExist:
        return JsonResponse({'error': 'Service request not found'}, status=404)