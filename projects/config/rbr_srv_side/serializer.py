from rest_framework import serializers
from .models import Server

from rest_framework import serializers
from .models import Server

'''
class ServerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Server
        fields = ['id', 'ip_address', 'description', 'name', 'server_is_active']
'''

class ServerSerializer1(serializers.ModelSerializer):

    class Meta:
        model = Server
        fields = ['name', 'ip_address', 'description', 'server_is_active', 'data_active']