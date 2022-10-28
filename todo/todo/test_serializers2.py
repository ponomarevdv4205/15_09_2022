from rest_framework import serializers
from test_models import User, Project, ToDo


class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    Email = serializers.CharField(max_length=128)


class ToDoSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=1024)
    user = UserSerializer()


class ProjectSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    users = UserSerializer(many=True)


user1 = User('Dima_1', 'ponomarevdv4205_1@yandex.ru')
serializer = UserSerializer(user1)
print(serializer.data)

todo = ToDo('Текст заметки', user1)
serializer = ToDoSerializer(todo)
print(serializer.data)

user2 = User('Dima_2', 'ponomarevdv4205_2@yandex.ru')
book = Project('Некоторая книга', [user1, user2])

serializer = ProjectSerializer(book)
print(serializer.data)

# cicle:
