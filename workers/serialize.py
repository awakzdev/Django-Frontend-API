from rest_framework import serializers
from .models import Worker, Paradigm, Job


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'hire_date', 'job_id',
                  'salary', 'commission_pct', 'manager_id', 'department_id', 'speciality']


class ParadigmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paradigm
        fields = ['id', 'url', 'speciality']


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'url', 'name', 'speciality']

