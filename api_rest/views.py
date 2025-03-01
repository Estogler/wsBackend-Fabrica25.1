from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .serializers import UsuarioSerializer
from .models import Usuario

import json

import requests

class UsuarioListCreat(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer



FIXER_API_KEY = "sua_chave_de_api"
FIXER_URL = "http://data.fixer.io/api/latest"

class Conversor(APIView):
    def post(self, request):
        response = requests.get(FIXER_URL, params={"access_key": FIXER_API_KEY})
        if response.status_code == 200:
            data = response.json()
            for currency, rate in data.get("rates", {}).items():
                Usuario.objects.create(currency=currency, rate=rate)
            return Response({"message": "Taxas salvas com sucesso!"}, status=status.HTTP_201_CREATED)
        return Response({"error": "Falha ao obter taxas."}, status=status.HTTP_400_BAD_REQUEST)
