from django.db import models

from doctor.models import Doctor


# Create your models here.

class HealthRecord(models.Model):
    patient_full_name = models.CharField(max_length=255, null=False, default='')
    patient_date_of_birth = models.DateField()
    patient_gender = models.CharField(max_length=255, null=False, default='')
    patient_address = models.CharField(max_length=255, null=False, default='')
    patient_nation = models.CharField(max_length=255, null=False, default='')
    patient_nationality = models.CharField(max_length=255, null=False, default='')
    patient_job = models.CharField(max_length=255, null=False, default='')
    patient_working_address = models.CharField(max_length=255, null=False, default='')
    patient_identify_number = models.CharField(max_length=255, null=False, default='')
    patient_health_ensurance_number = models.CharField(max_length=255, null=False, default='')
    patient_homie = models.CharField(max_length=255, null=False, default='')
    patient_homie_phone = models.CharField(max_length=255, null=False, default='')
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    health_record_date = models.DateTimeField(auto_now_add=True)
    diagnose = models.TextField(null=False, default='')
    health_record_description = models.TextField(null=False, default='')

    def __str__(self):
        return str(self.id) + '/' + self.patient_identify_number + ' / ' + self.patient_full_name

    class Meta:
        db_table = "health_records"
        verbose_name = 'Health Record'
        verbose_name_plural = 'Health Records'