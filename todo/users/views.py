from urllib import request
from .serializers import UserModelSerializer, ProjectModelSerializer, ToDoHyperlinkedModelSerializer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, BasePermission
from .filters import ProjectFilter
from .models import User, Project, ToDo
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.settings import api_settings


class AdminOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class UserViewSet(RetrieveModelMixin,
                        ListModelMixin,
                        UpdateModelMixin,
                        GenericViewSet):
    # permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


# class CustomUserModelViewSet(ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserModelSerializer
class CustomLimitOffsetPagination(LimitOffsetPagination):

    def __init__(self, default_limit=api_settings.PAGE_SIZE, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default_limit = default_limit


class ViewPaginatorMixin:
    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                if getattr(self, 'paginate_limit', None):
                    self._paginator = self.pagination_class(
                        default_limit=getattr(self, 'paginate_limit', None))
                else:
                    self._paginator = self.pagination_class()
        return self._paginator


class ToDoModelViewSet(ViewPaginatorMixin, ModelViewSet):
    queryset = ToDo.objects.filter(is_active=True)
    serializer_class = ToDoHyperlinkedModelSerializer
    filterset_fields = ['project']
    paginate_limit = 2
    pagination_class = CustomLimitOffsetPagination

    def destroy(self, request, *args, **kwargs):
        todo = self.get_object()
        todo.is_active = False
        todo.save()


class ProjectDjangoFilterViewSet(ViewPaginatorMixin, ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_class = ProjectFilter
    paginate_limit = 2
    pagination_class = CustomLimitOffsetPagination


# -------------------- Обычное отображение -------------------------------------
class UserModelViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer] # Коммент специально, т.к. выводит формат JSON
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


# class ToDoModelViewSet(ModelViewSet):
#     queryset = ToDo.objects.all()
#     serializer_class = ToDoHyperlinkedModelSerializer
