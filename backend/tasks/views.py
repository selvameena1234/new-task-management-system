from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

# GET TASKS
@api_view(['GET'])
def get_tasks(request):
    tasks = Task.objects.all()

    user_id = request.GET.get('user')
    status = request.GET.get('status')

    if user_id:
        tasks = tasks.filter(assigned_to_id=user_id)

    if status:
        tasks = tasks.filter(status=status)

    return Response(TaskSerializer(tasks, many=True).data)


# UPDATE STATUS (USER ONLY)
@api_view(['PATCH'])
def update_task(request, pk):
    task = Task.objects.get(id=pk)
    task.status = request.data.get('status', task.status)
    task.save()
    return Response(TaskSerializer(task).data)


# CREATE TASK (ADMIN ONLY - SIMPLE CHECK)
@api_view(['POST'])
def create_task(request):
    role = request.data.get('role')

    if role != 'admin':
        return Response({"error": "Only admin can create tasks"}, status=403)

    task = Task.objects.create(
        title=request.data['title'],
        description=request.data['description'],
        assigned_to_id=request.data['assigned_to'],
        created_by_id=request.data['created_by']
    )
    return Response(TaskSerializer(task).data)