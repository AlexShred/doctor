from django.urls import path

from . import views

urlpatterns = (
    path('doctor/', views.doctor_list_create_api_view),
    path('doctor/<int:pk>', views.DoctorRetrieveUpdataDestroyView.as_view()),
    path('patient/', views.patient_list_create_api_view),
    path('patient/<int:pk>', views.PatientRetrieveUpdataDestroyView.as_view()),
)