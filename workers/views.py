from .models import Worker, Speciality
from .serializers import WorkerSerializer, SpecialitySerializer
from rest_framework import viewsets
from rest_framework.views import APIView


class SpecialityView(viewsets.ModelViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer


class WorkerView(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
