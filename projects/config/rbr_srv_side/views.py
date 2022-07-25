from rest_framework import generics
#from .serializer import ServerSerializer
from .serializer import ServerSerializer1
from .models import Server

'''
class ServerViewSet(generics.ListAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializer

class ServerAddView(generics.CreateAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializer

class ServerDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializer
'''

class ServerViewSet1(generics.ListAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializer1

class ServerAddView1(generics.CreateAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializer1

class ServerDetailView1(generics.RetrieveUpdateDestroyAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializer1
