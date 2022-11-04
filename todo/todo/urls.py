"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import include, path, re_path
# from rest_framework.routers import DefaultRouter, SimpleRouter
# # ,UserModelViewSet, ProjectModelViewSet,
# from users.views import UserViewSet, ToDoModelViewSet, ProjectDjangoFilterViewSet, \
#     UserModelViewSet, ProjectModelViewSet, ToDoDjangoFilterViewSet
# # from rest_framework import permissions
# # from drf_yasg.views import get_schema_view
# # from drf_yasg import openapi
#
# router = DefaultRouter()
# # router = SimpleRouter()
# router.register('users', UserModelViewSet) # Обычное отображение
# router.register('projects', ProjectModelViewSet) # Обычное отображение
# router.register('todos', ToDoModelViewSet) # Обычное отображение
# # router.register('users', UserViewSet) # Настроенное отображение / отображение с фильтрами
# # router.register('projects', ProjectDjangoFilterViewSet) # Настроенное отображение / отображение с фильтрами
# # router.register('todos', ToDoDjangoFilterViewSet) # Настроенное отображение / отображение с фильтрами
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls')), # Это включает авторизацию
# ]

from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
# ,CustomUserModelViewSet, ProjectModelViewSet,
from users.views import UserViewSet, ToDoModelViewSet, ProjectDjangoFilterViewSet
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

router = DefaultRouter()
router.register('users', UserViewSet)
# router.register('users', CustomUserModelViewSet)
# router.register('projects', ProjectModelViewSet)
router.register('projects', ProjectDjangoFilterViewSet)
router.register('todo', ToDoModelViewSet)

# schema_view = get_schema_view(
#     openapi.Info(
#         title="Snippets API",
#         default_version='v1',
#         description="Test description",
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="contact@snippets.local"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token/', obtain_auth_token),
]
