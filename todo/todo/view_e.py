from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes, action
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet, GenericViewSet
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, get_object_or_404

# from users.filters import ProjectFilter
# from users.filters import ProjectFilter
from users.filters import ProjectFilter
from users.models import Project
from users.serializers import ProjectModelSerializer


# level 1 APIView
class ProjectAPIView(APIView):
    # renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
    # http://127.0.0.1:8000/api/project
    def get(self, request, format=None):
        project = Project.objects.all()
        serializer = ProjectModelSerializer(project, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        pass


# #
@api_view(['GET'])  ##'POST'
# @renderer_classes([JSONRenderer,BrowsableAPIRenderer])
def get(request):
    if request.method == 'GET':
        project = Project.objects.all()
        serializer = ProjectModelSerializer(project, many=True)
        # return Response(serializer.data)
        return Response({'test': 1})  ###Дополнительный пример
    elif request.method == 'POST':
        pass


# level 2 Generic views
class ProjectCreateAPIView(CreateAPIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class ProjectListAPIView(ListAPIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


# #
class ProjectRetrieveAPIView(RetrieveAPIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


#
class ProjectDestroyAPIView(DestroyAPIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class ProjectUpdateAPIView(UpdateAPIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


# level 3 ViewSets

class ProjectViewSet(ViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    # {"name": "test",
    #  "users": [2, 3]}
    def post(self, request):
        project = ProjectModelSerializer(data=request.data)
        project.is_valid()
        project.save()
        return Response(project.data)

    def list(self, request):  # список
        project = Project.objects.all()
        serializer_class = ProjectModelSerializer(project, many=True)
        return Response(serializer_class.data)

    def retrieve(self, request, pk=None):  # детализация
        project = get_object_or_404(Project, pk=pk)
        serializer_class = ProjectModelSerializer(project)
        return Response(serializer_class.data)

    def destroy(self, request, pk=None):
        instance = get_object_or_404(Project, pk=pk)
        instance.delete()
        project = Project.objects.all()
        serializer_class = ProjectModelSerializer(project, many=True)
        return Response(serializer_class.data)

    #
    @action(detail=True, methods=['get'])
    def only(self, request, pk=None):
        project = Project.objects.get(id=pk)
        return Response({'project': project.name, 'id': project.id})


# level 4 ModelViewSet (то что мы делали изначально самый просто способ)
class ProjectModelViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


# level 5 Custom ViewSet
#
# ListModelMixin, CreateAPIView, DestroyModelMixin, RetrieveAPIView, UpdateAPIView, GenericViewSet:
class ProjectCustomViewSet(ListModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]


# filter
class ProjectQuerysetFilterViewSet(ModelViewSet):
    serializer_class = ProjectModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()

    def get_queryset(self):
        return Project.objects.filter(name__contains='te1')  # содержит


# #
#
class ProjectFilterListAPIView(ListAPIView):
    serializer_class = ProjectModelSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return Project.objects.filter(name__contains=name)


class ProjectFilterModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', '')
        project = Project.objects.all()
        if name:
            project = project.filter(name__contains=name)
        return project


# DjangoFilter
# filters.py ПОКАЗАТЬ НЕ ЗАБЫТЬ
class ProjectDjangoFilterViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    # filterset_fields = ['id','name']
    filterset_class = ProjectFilter


# # #PAGINATOR
class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2


# # # # # #
# # # # # #
class ProjectLimitOffsetPaginatonViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination
    # ProjectLimitOffsetPagination
