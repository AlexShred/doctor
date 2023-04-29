from django.urls import path

from . import views

urlpatterns = (
    path('doctor/', views.doctor_list_create_api_view),
    path('patient/', views.patient_list_create_api_view),
    path('patient/<int:pk>', views.patient_retrieve_updata_destroy_api_view),
)