import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .test_models import User


class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    Email = serializers.CharField(max_length=128)


def start():
    # Преобразования:
    user = User('Dima', 'ponomarevdv4205@yandex.ru')
    serializer = UserSerializer(user)
    print(serializer.data)
    print(type(serializer.data))

    print(50 * '*')
    renderer = JSONRenderer()
    json_bytes = renderer.render(serializer.data)
    print(json_bytes)
    print(type(json_bytes))
    # Обратное преобразования
    print(50 * '*')
    stream = io.BytesIO(json_bytes)
    print(stream)
    data = JSONParser().parse(stream)  # dict
    print(data)
    print(type(data))
    #
    # #Восстановить объект
    print(50 * '*')
    serializer = UserSerializer(data=data)
    print(serializer.is_valid())  # Подобие формы
    print(serializer.validated_data)
    print(type(serializer.validated_data))


start()
