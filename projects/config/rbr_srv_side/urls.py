# Файл rbr_srv_side/urls.py

from django.urls import path
# from .views import ServerDetailView, ServerAddView, ServerViewSet
from .views import ServerDetailView1, ServerAddView1, ServerViewSet1


urlpatterns = [
    path('servers/', ServerViewSet1.as_view()),
    path('servers/<int:pk>', ServerDetailView1.as_view()),
    path('servers/add', ServerAddView1.as_view()),
    path('servers/status', ServerViewSet1.as_view()),
]