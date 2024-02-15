from rest_framework import serializers

# pylint: disable=import-error
from userlist.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
