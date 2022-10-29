from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

# from users.views import UserViewSet, ProjectViewSet, ToDoViewSet
# from todo.view_exam import ProjectViewSet
# from todo.view_example import ProjectListAPIView


# from todo.view_example import get
# from todo.view_example import ProjectViewSet
# ProjectLimitOffsetPaginatonViewSet
# from todo.view_example import get
# from todo.view_example import ProjectCustomViewSet
# from todo.view_example import ProjectListAPIView
from todo.view_e import ProjectLimitOffsetPaginatonViewSet
# from todo.view_example import ProjectAPIView
# from todo.view_exam import ProjectModelViewSet

# from todo.view_exam import ProjectDjangoFilterViewSet
# from todo.view_exam import ProjectAPIView
# from todo.view_exam import get
# from todo.view_exam import ProjectCustomViewSet
from todo.view_e import ProjectAPIView, get, ProjectViewSet, ProjectModelViewSet, ProjectCustomViewSet, \
    ProjectQuerysetFilterViewSet, ProjectFilterListAPIView, ProjectFilterModelViewSet, ProjectDjangoFilterViewSet

router = DefaultRouter()
# from todo.view_example import ProjectModelViewSet
# from todo.view_example import ProjectModelViewSet
router.register('project_model_view', ProjectDjangoFilterViewSet)

# router = SimpleRouter()
# router.register('project_f', ProjectDjangoFilterViewSet)
router.register('project_p', ProjectLimitOffsetPaginatonViewSet)
# router.register('todo', ToDoViewSet)


from todo.view_e import ProjectCreateAPIView, ProjectRetrieveAPIView, ProjectDestroyAPIView, ProjectListAPIView, \
    ProjectUpdateAPIView

# level 3
# router.register('project', ProjectViewSet, basename='project')
#
# # level 4
# router.register('project_model', ProjectModelViewSet)
#
# # level 5
# router.register('project_custom', ProjectCustomViewSet)
#
# #Filter
# router.register('project_filter', ProjectQuerysetFilterViewSet)
#
# router.register('project', ProjectViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('api/', include(router.urls)),

    # level 1
    # path('api/project', ProjectAPIView.as_view()),
    # path('api/project_get', get),
    #
    # # level 2
    # path('api/list/', ProjectListAPIView.as_view()),
    # path('api/create/', ProjectCreateAPIView.as_view()),
    # path('api/update/<int:pk>/', ProjectUpdateAPIView.as_view()),
    # path('api/delete/<int:pk>/', ProjectDestroyAPIView.as_view()),
    # path('api/detail/<int:pk>/', ProjectRetrieveAPIView.as_view()),

    # # level 3 - 5
    path('api/', include(router.urls)),

    # filter part_2
    path('api/<str:name>/', ProjectFilterListAPIView.as_view()),
    #
    # path('api/', include(router.urls)),
]
# Footer
