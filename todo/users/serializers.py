###########################################################################################################
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


class ToDoHyperlinkedModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'


class ProjectModelSerializer(ModelSerializer):
    # users = StringRelatedField(many=True) #Делает список юзеров в Тексте

    class Meta:
        model = Project
        fields = '__all__'


#####################################################################################################

from django.db.models import ManyToManyField
from django.forms import URLField

from users.models import User
# from users.serializers import UserModelSerializer
from .models import Project, ToDo, User
from rest_framework.serializers import ModelSerializer, Serializer, CharField, EmailField, StringRelatedField


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserModelSerializer(Serializer):
    firstname = CharField(max_length=60)
    lastname = CharField(max_length=60)
    email = EmailField(default=None)

    def update(self, instance, validated_data):
        instance.firstname = validated_data.get('firstname', instance.first_name)
        instance.lastname = validated_data.get('lastname', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

    def create(self, validated_data):
        user = User(**validated_data)
        user.save()
        return user


class ProjectSerializer(ModelSerializer):
    user = StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class ToDoSerializer(ModelSerializer):
    user = StringRelatedField(many=False)
    project = StringRelatedField(many=False)

    class Meta:
        model = ToDo
        fields = ['text', 'user', 'project']
