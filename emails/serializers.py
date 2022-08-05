from rest_framework.serializers import IntegerField, Serializer, CharField, EmailField


class SendRequestSerializer(Serializer):
    email = EmailField(required=True, allow_null=False)
    password = CharField(max_length=32, min_length=4, required=True, allow_null=False)
    limit = IntegerField(min_value=500, max_value=2000, required=True)


class LoginRequestSerializer(Serializer):
    email = EmailField(required=True, allow_null=False)
    password = CharField(max_length=32, min_length=4, required=True, allow_null=False)
