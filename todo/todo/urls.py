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
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter, SimpleRouter
# ,UserModelViewSet, ProjectModelViewSet,
from users.views import UserViewSet, ToDoModelViewSet, ProjectDjangoFilterViewSet, \
    UserModelViewSet, ProjectModelViewSet, ToDoDjangoFilterViewSet
# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

router = DefaultRouter()
# router = SimpleRouter()
router.register('users', UserModelViewSet) # Обычное отображение
router.register('projects', ProjectModelViewSet) # Обычное отображение
router.register('todos', ToDoModelViewSet) # Обычное отображение
# router.register('users', UserViewSet) # Настроенное отображение / отображение с фильтрами
# router.register('projects', ProjectDjangoFilterViewSet) # Настроенное отображение / отображение с фильтрами
# router.register('todos', ToDoDjangoFilterViewSet) # Настроенное отображение / отображение с фильтрами

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
