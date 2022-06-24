from django.db import models


class Speciality(models.Model):
    paradigm = models.CharField(max_length=50)

    def __str__(self):
        return self.paradigm


class Worker(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.IntegerField(default=0)
    hire_date = models.DateField()
    job = models.CharField(max_length=100)
    speciality = models.ManyToManyField(Speciality, blank=True)
    salary = models.IntegerField(default=0)
    commission_pct = models.IntegerField(default=0, blank=True, null=True)
    manager_id = models.IntegerField(default=0, blank=True, null=True)
    department_id = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.name
