from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import views
from rest_framework.generics import get_object_or_404


from .models import Doctor, Patient
from .my_generic import MyGenericRetriveUpdataDestroyView
from .serializers import DoctorSerializer, PatientSerializer


@api_view(http_method_names=['POST', 'GET'])
def doctor_list_create_api_view(request):
    if request.method == "GET":
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(instance=doctors, many=True)
        return Response(serializer.data, status=200)
    if request.method == "POST":
        received_data = request.data
        serializer = DoctorSerializer(data=received_data)

        if serializer.is_valid():
            doctor=serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


class DoctorRetrieveUpdataDestroyView(views.APIView):

    def get_object(self, pk):
        return get_object_or_404(Doctor, pk=pk)

    def get(self, request, pk, *args, **kwargs):
        serializer = DoctorSerializer(instance=self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        serializer = DoctorSerializer(instance=self.get_object(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=404)

    def delete(self, request, pk, *args, **kwargs):
        self.get_object(pk).delete()
        return Response(status=204)


@api_view(http_method_names=['GET', 'POST'])
def patient_list_create_api_view(request):
    if request.method == 'GET':
        pat_set = Patient.objects.all()
        serializer = PatientSerializer(pat_set, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


class PatientRetrieveUpdataDestroyView(MyGenericRetriveUpdataDestroyView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
