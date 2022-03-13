from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserFilterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'is_active',
                  'is_superuser', 'date_joined', 'last_login',)
