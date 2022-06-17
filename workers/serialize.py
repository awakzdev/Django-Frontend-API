from rest_framework import serializers
from .models import Worker


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'hire_date', 'job_id',
                  'salary', 'commission_pct', 'manager_id', 'department_id']
