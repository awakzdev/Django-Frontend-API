from django.shortcuts import render
from .models import Worker
from .serialize import WorkerSerializer
from rest_framework import viewsets, permissions


class WorkerView(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
