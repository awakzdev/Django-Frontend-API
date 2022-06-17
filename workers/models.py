from django.db import models


class Worker(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.IntegerField(default=0)
    hire_date = models.DateField(auto_now=True)
    job_id = models.CharField(max_length=20)
    salary = models.IntegerField(default=0)
    commission_pct = models.IntegerField(default=0)
    manager_id = models.IntegerField(default=0)
    department_id = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.name
