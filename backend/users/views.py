from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User

@api_view(['GET'])
def users_list(request):
    users = User.objects.all().values('id', 'username', 'role')
    return Response(users)