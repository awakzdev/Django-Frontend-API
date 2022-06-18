from django.db import models


class Paradigm(models.Model):
    speciality = models.CharField(max_length=50)

    def __str__(self):
        return self.speciality


class Worker(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.IntegerField(default=0)
    hire_date = models.DateField(auto_now=True)
    job_id = models.CharField(max_length=100)
    speciality = models.ForeignKey(Paradigm, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    commission_pct = models.IntegerField(default=0, blank=True)
    manager_id = models.IntegerField(default=0, blank=True)
    department_id = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.first_name


class Job(models.Model):
    name = models.CharField(max_length=50)
    speciality = models.ManyToManyField(Paradigm)

    def __str__(self):
        return self.name
