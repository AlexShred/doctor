from django.db import models


class Doctor(models.Model):
    name_doctor = models.CharField(max_length=30)
    experience = models.FloatField()

    def __str__(self):
        return self.name_doctor


class Patient(models.Model):
    fullname = models.CharField(max_length=30)
    purpose_visit = models.CharField(max_length=30)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname
