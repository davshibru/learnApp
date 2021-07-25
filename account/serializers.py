from rest_framework import serializers
from .models import Account

class CheckFirstLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['id', 'username','is_it_first_login', 'is_password_had_changed', 'is_staff']

class UserForAccessSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['id', 'username']

class setFirstLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('username', 'password', 'email', 'is_admin', 'is_superuser', 'is_staff')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Account(**validated_data)
        user.set_password(password)
        user.save()
        return user

class ChangePasswordSerializer(serializers.Serializer):

    model = Account

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class GetUserIdSerializer(serializers.Serializer):

    class Meta:
        model = Account
        fields = ['id']
