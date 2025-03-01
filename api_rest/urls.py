from django.urls import path
from .views import UsuarioListCreat, UsuarioDetail, Conversor

urlpatterns = [
    path('criar/', UsuarioListCreat.as_view(), name='criar'),
    path('detalhes/<int:pk>/', UsuarioDetail.as_view(), name='detalhes'),
    path('fetch-rates/', Conversor.as_view(), name='fetch-rates'),

]
