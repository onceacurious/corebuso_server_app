from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class AccountSerializer(ModelSerializer):
    """Account serializer intended only for admin user"""
    class Meta:
        model = User
        fields = '__all__'


class AccountFrontendSerializer(ModelSerializer):
    """For frontend authentication"""
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance