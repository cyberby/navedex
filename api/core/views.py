from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Project, Naver
from .serializers import ProjectSerializer, NaverSerializer, UserSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

class NaverViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Naver.objects.filter(user=self.request.user)
    serializer_class = NaverSerializer
    queryset = Naver.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'admission_date', 'job_role']

class UserView(generics.CreateAPIView):
    permission_classes = []
    serializer_class = UserSerializer
