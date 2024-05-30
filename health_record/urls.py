from django.urls import path
from . import views

urlpatterns = [
    path('add_health_record', views.add_health_record, name='add_health_record'),
    path('health_record_detail/<int:id>', views.health_record_detail, name='health_record_detail'),
    path('health_record_edit/<int:id>', views.health_record_edit, name='health_record_edit'),
    path('health_record_delete/<int:id>', views.health_record_delete, name='health_record_delete'),
]
