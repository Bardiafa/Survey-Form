from django.shortcuts import render

from rest_framework import viewsets

from .models import Form
from .serializers import FormSerializer

class FormViewSet(viewsets.ModelViewSet):

    serializer_class = FormSerializer
    queryset = Form.objects.all()

    def perform_create(self, serializer):
        serializer.save()
