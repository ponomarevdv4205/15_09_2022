from .serializers import UserModelSerializer, ProjectModelSerializer, ToDoHyperlinkedModelSerializer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, UpdateModelMixin
from rest_framework.pagination import LimitOffsetPagination
from .filters import ProjectFilter
from .models import User, Project, ToDo
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer


class UserViewSet(ListModelMixin, UpdateModelMixin, GenericViewSet):
    # renderer_classes = [JSONRenderer] # Коммент специально, т.к. выводит формат JSON
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class ToDoDjangoFilterViewSet(ModelViewSet, LimitOffsetPagination):
    queryset = ToDo.objects.filter(is_active=True)
    serializer_class = ToDoHyperlinkedModelSerializer
    filterset_fields = ['project']
    limit = LimitOffsetPagination
    limit.default_limit = 20
    pagination_class = limit

    def destroy(self, request, *args, **kwargs):
        todo = self.get_object()
        todo.is_active = False
        todo.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProjectDjangoFilterViewSet(ModelViewSet, LimitOffsetPagination):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_class = ProjectFilter
    limit = LimitOffsetPagination
    limit.default_limit = 10
    pagination_class = limit


# -------------------- Обычное отображение -------------------------------------
class UserModelViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer] # Коммент специально, т.к. выводит формат JSON
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoHyperlinkedModelSerializer
