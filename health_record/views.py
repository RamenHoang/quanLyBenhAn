from django.shortcuts import render, redirect

from doctor.models import Doctor
from health_record.models import HealthRecord


# Create your views here.

def add_health_record(request):
    """
    Add health record view
    """
    if request.user.is_authenticated is False:
        return redirect('login')

    if request.method == 'POST':
        health_record = HealthRecord.objects.create(
            patient_full_name=request.POST['patient_full_name'],
            patient_date_of_birth=request.POST['patient_date_of_birth'],
            patient_gender=request.POST['patient_gender'],
            patient_address=request.POST['patient_address'],
            patient_nation=request.POST['patient_nation'],
            patient_nationality=request.POST['patient_nationality'],
            patient_job=request.POST['patient_job'],
            patient_working_address=request.POST['patient_working_address'],
            patient_identify_number=request.POST['patient_identify_number'],
            patient_health_ensurance_number=request.POST['patient_health_ensurance_number'],
            patient_homie=request.POST['patient_homie'],
            patient_homie_phone=request.POST['patient_homie_phone'],
            doctor=Doctor.objects.get(id=request.POST['doctor_id']),
            diagnose=request.POST['diagnose'],
            health_record_description=request.POST['health_record_description'],
        )

        return redirect('home')

    doctors = Doctor.objects.all()

    return render(request, 'add_health_record.html', {'doctors': doctors})


def health_record_detail(request, id):
    """
    Health record detail view
    """
    if request.user.is_authenticated is False:
        return redirect('login')

    health_record = HealthRecord.objects.get(id=id)
    doctors = Doctor.objects.all()

    return render(request, 'view_health_record.html', {'health_record': health_record, 'doctors': doctors})


def health_record_edit(request, id):
    """
    Health record detail view
    """
    if request.user.is_authenticated is False:
        return redirect('login')

    if request.method == 'POST':
        HealthRecord.objects.filter(id=id).update(
            patient_full_name=request.POST['patient_full_name'],
            patient_date_of_birth=request.POST['patient_date_of_birth'],
            patient_gender=request.POST['patient_gender'],
            patient_address=request.POST['patient_address'],
            patient_nation=request.POST['patient_nation'],
            patient_nationality=request.POST['patient_nationality'],
            patient_job=request.POST['patient_job'],
            patient_working_address=request.POST['patient_working_address'],
            patient_identify_number=request.POST['patient_identify_number'],
            patient_health_ensurance_number=request.POST['patient_health_ensurance_number'],
            patient_homie=request.POST['patient_homie'],
            patient_homie_phone=request.POST['patient_homie_phone'],
            doctor=Doctor.objects.get(id=request.POST['doctor_id']),
            diagnose=request.POST['diagnose'],
            health_record_description=request.POST['health_record_description'],
        )

        return redirect('health_record_detail', id=id)

    health_record = HealthRecord.objects.get(id=id)
    doctors = Doctor.objects.all()

    return render(request, 'edit_health_record.html', {'health_record': health_record, 'doctors': doctors})

def health_record_delete(request, id):
    """
    Health record delete view
    """
    if request.user.is_authenticated is False:
        return redirect('login')

    HealthRecord.objects.filter(id=id).delete()

    return redirect('home')