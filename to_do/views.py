from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from to_do.models import ToDoList
from to_do.serializers import ToDoListSerializer


@api_view(['GET', 'POST'])
def get_list(request):
    if request.method == 'GET':
        to_do_list = ToDoList.objects.all()
        serializer = ToDoListSerializer(to_do_list, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ToDoListSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def list_detail(request, pk):
    if request.method == 'GET':
        to_do_list = ToDoList.objects.get(pk=pk)
        serializer = ToDoListSerializer(to_do_list)
        return Response(serializer.data)
    if request.method == 'PUT':
        to_do_list = ToDoList.objects.get(pk=pk)
        serializer = ToDoListSerializer(data=request.data, instance=to_do_list)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    if request.method == 'DELETE':
        to_do_list = ToDoList.objects.get(pk=pk)
        to_do_list.delete()
        return Response('Deleted')
