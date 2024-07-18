from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Task
from .serializers import TasksSearializer

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/task-list/',
        'Detail View':'/task-detail/<str:pk>',
        'Create':'/task-detail/<str:pk>',
        'Update':'/task-detail/<str:pk>',
        'Delete':'/task-detail/<str:pk>',
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TasksSearializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetails(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TasksSearializer(tasks, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = TasksSearializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TasksSearializer(instance=task,data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response("Item Sucessfully Deleted!!!")