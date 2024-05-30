from django.contrib import admin

from doctor.models import Doctor, Speciality

# Register your models here.

admin.site.register(Doctor)
admin.site.register(Speciality)