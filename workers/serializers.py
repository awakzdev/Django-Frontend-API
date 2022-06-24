from rest_framework import serializers
from .models import Worker, Speciality


class SpecialitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Speciality
        fields = ['id', 'url', 'paradigm']


class WorkerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Worker
        fields = ['id', 'url', 'name', 'last_name', 'hire_date', 'email', 'phone_number', 'job', 'speciality', 'salary',
                  'commission_pct', 'manager_id', 'department_id']
