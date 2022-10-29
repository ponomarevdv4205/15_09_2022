from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet

# Create your views here.


from .serializers import UserModelSerializer, ProjectModelSerializer, ToDoHyperlinkedModelSerializer
from .models import User, Project, ToDo


class UserModelViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer] # Коммент специально
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoHyperlinkedModelSerializer
