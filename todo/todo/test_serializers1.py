import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from test_models import User


class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    Email = serializers.CharField(max_length=128)

    def create(self, validated_data):
        return User(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.Email = validated_data.get('Email', instance.Email)
        return instance

    # def validate_Email(self, value):
        if len(value) < 100:
            raise serializers.ValidationError('Email уже большой!')
        return value

    # Закоментировали как в лекции:
    # def validate(self, attrs):
    #     if attrs['name'] == 'Dima_1' and attrs['Email'] != 'ponomarevdv4205_1@yandex.ru':
    #         raise serializers.ValidationError('Неверный Email')
    #     return attrs


def start():
    user = User('Dima_1', 'ponomarevdv4205_1@yandex.ru')
    serializer = UserSerializer(user)

    renderer = JSONRenderer()
    json_bytes = renderer.render(serializer.data)

    stream = io.BytesIO(json_bytes)
    data = JSONParser().parse(stream)

    serializer = UserSerializer(data=data)
    serializer.is_valid()
    # Продолжение скрипта №1

    # Создание
    user = serializer.save()
    print(type(user))
    print(user)

    # Обновление всех данных
    data = {'name': 'Dima_1', 'Email': 'ponomarevdv4205_1@yandex.ru'}
    serializer = UserSerializer(user, data=data)
    serializer.is_valid()
    user = serializer.save()
    print(user)

    # Обновление частичное
    data = {'Email': 'ponomarevdv4205_1@yandex.ru'}
    serializer = UserSerializer(user, data=data, partial=True)
    serializer.is_valid()
    user = serializer.save()
    print(f'{user} {user.Email}')

    # Проверка 1го поля
    data = {'Email': 'ponomarevdv4205_1@yandex.ru'}
    serializer = UserSerializer(user, data=data, partial=True)
    if serializer.is_valid():
        user = serializer.save()
        print(f'{user} {user.Email}')
    else:
        print(serializer.errors)

    # Проверка всех полей
    data = {'name': 'Dima_1', 'Email': 'ponomarevdv4205_1@yandex.ru'}
    serializer = UserSerializer(user, data=data)
    if serializer.is_valid():
        user = serializer.save()
        print(user)
    else:
        print(serializer.errors)


start()
