from rest_framework.serializers import ModelSerializer
from users.models import User


class UserSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class CustomUserSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']
