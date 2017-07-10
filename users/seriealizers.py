from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers


class UserListSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()


class UserSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.EmailField()

    def create(self, validated_data):
        """
        Creamos una instancia de user a partir de los datos en validated_data
        que contiene los valores deserealizados
        :param validated_data: Diccionario con datos de usuario
        :return: Objeto User
        """
        instance = User()
        return self.update(instance,validated_data)

    def update(self, instance, validated_data):

        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.password = make_password(validated_data.get('password'))
        instance.email = validated_data.get('email')
        instance.save()
        return instance

    def validate_username(self, username):
        #username = super().validate_username(username)
        if (self.instance is None or self.instance.username != username) and \
                User.objects.filter(username=username).exists():
            raise ValidationError("El nombre de usuario {0} ya exite".format(username))
        return username

    def validate_email(self, email):
        #email = super().validate_email(email)
        if (self.instance is None or self.instance.username != email) and \
                User.objects.filter(username=email).exists():
            raise ValidationError("El email {0} ya existe".format(email))
        return email