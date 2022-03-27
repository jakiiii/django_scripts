from rest_framework import serializers
from apps.authotp.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'is_verified')


class VerifyUserSerializers(serializers.Serializer):
    email = serializers.EmailField(max_length=32)
    otp = serializers.CharField(max_length=6)
