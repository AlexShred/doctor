from rest_framework import serializers

from .models import Doctor, Patient


class DoctorSerializer(serializers.Serializer):
    name_doctor = serializers.CharField()
    experience = serializers.CharField()

    def create(self, validated_data):
        return Doctor.objects.create(
            name_doctor=validated_data['name_doctor'],
            experience=validated_data['experience']
        )

    def update(self, instance, validated_data):
        instance.content = validated_data['name_doctor']
        instance.created = validated_data['experience']
        return instance


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"
