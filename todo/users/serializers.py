from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, StringRelatedField

from .models import User, Project, ToDo


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # fields = ('firstname','lastname')
        # exclude = ('firstname',)


class ToDoHyperlinkedModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'


class ProjectModelSerializer(ModelSerializer):
    # users = StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = '__all__'