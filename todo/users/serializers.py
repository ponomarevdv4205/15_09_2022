from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, StringRelatedField
from django.contrib.auth.hashers import make_password
from .models import User, Project, ToDo


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(self, UserModelSerializer).create(validated_data)


class ToDoModelSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'


class ProjectModelSerializer(ModelSerializer):
    # users = StringRelatedField(many=True) #Делает список юзеров в Тексте

    class Meta:
        model = Project
        fields = '__all__'
