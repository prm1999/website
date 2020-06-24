from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import student
from .serializer import studentSerializer


class studentList(APIView):

    def get(self, request):
        student1 = student.objects.all()
        serializer = studentSerializer(student1, many=True)
        return Response(serializer.data)

    def post(self):
        pass

# Create your views here.
