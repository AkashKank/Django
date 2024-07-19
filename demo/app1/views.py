from django.shortcuts import render
from rest_framework.response import  Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializers
# Create your views here.

class EmployeeDetails(APIView):

    def get(self, request, id=None):
        if id:
            try:
                obj = Employee.objects.get(id=id)
                serializer = EmployeeSerializers(obj)
                return Response(serializer.data)
            except:
                msg = {"msg":"Not Found"}
                return Response(msg, status=status.HTTP_404_NOT_FOUND)    
        
        else:
            obj = Employee.objects.all()
            serialzier = EmployeeSerializers(obj, many=True)
            return Response(serialzier.data, status=status.HTTP_200_OK)


    def post(self, request):
        serialzier = EmployeeSerializers(data=request.data)
        if serialzier.is_valid():
            serialzier.save()
            return Response(serialzier.data, status=status.HTTP_201_CREATED)
        return Response(serialzier.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def put(self, request, pk=None):
    #     try:
    #         item = Item.objects.get(pk=pk)
    #     except Item.DoesNotExist:
    #         return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
    #     serializer = ItemSerializer(item, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def put(self, request, id=id):
        try:
            obj = Employee.objects.get(id = id)
        except Employee.DoesNotExist:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        serialzier = EmployeeSerializers(obj, data=request.data, partial=True)
        if serialzier.is_valid():
            serialzier.save()
            return Response(serialzier.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serialzier.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=id):
        try:
            obj =Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            msg = {"msg":"not Found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        obj.delete()
        return Response({"msg":"Deleted Sucessfully"},status=status.HTTP_204_NO_CONTENT)



    



