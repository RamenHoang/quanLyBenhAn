from django.db import models

# Create your models here.

class Speciality(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Speciality'
        verbose_name_plural = 'Specialities'
        db_table = "specialities"

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    speciality = models.ForeignKey(Speciality, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "doctors"
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'
