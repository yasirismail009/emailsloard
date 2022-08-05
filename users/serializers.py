from rest_framework.serializers import ModelSerializer, Serializer, CharField, EmailField
from users.models import User


class RegisterRequestSerializer(Serializer):
    email = EmailField(required=True, allow_null=False)
    password = CharField(max_length=32, min_length=4, required=True, allow_null=False)
    first_name = CharField(max_length=32, min_length=3, required=True, allow_null=False)
    last_name = CharField(max_length=32, min_length=3, required=True, allow_null=False)


class LoginRequestSerializer(Serializer):
    email = EmailField(required=True, allow_null=False)
    password = CharField(max_length=32, min_length=4, required=True, allow_null=False)


class UserSerializer(ModelSerializer):
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'is_active', 'settings']
