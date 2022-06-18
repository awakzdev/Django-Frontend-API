from django.shortcuts import render
from .models import Worker, Paradigm, Job
from .serialize import WorkerSerializer, ParadigmSerializer, JobSerializer
from rest_framework import viewsets, permissions


class WorkerView(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer


class JobView(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer



