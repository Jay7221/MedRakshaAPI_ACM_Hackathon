from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse, Http404
from medicine.models import Medicine
from medicine.serializers import MedicineSerializer
from django.db.models import Q
from rest_framework.views import APIView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@api_view(['POST'])
def loginUser(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({"success" : "true"})
    else:
        return Response({"success" : "false"})