from django.urls import path

from . import views

urlpatterns = (
    path('doctor/', views.doctor_list_create_api_view),
    path('patient/', views.PatientListCreateAPIView.as_view()),
)