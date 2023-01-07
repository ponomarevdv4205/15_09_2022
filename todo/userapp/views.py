from rest_framework import generics
from users.models import User
from userapp.serializers import UserSerializers, CustomUserSerializers


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def get_serializer_class(self):
        if self.request.version == 'v1':
            return UserSerializers
        return CustomUserSerializers