from rest_framework.serializers import ModelSerializer
from .models import *

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class ResidencyAddressHistorySerializer(ModelSerializer):
    class Meta:
        model = ResidencyAddressHistory
        fields = "__all__"

class StudentProgramSerializer(ModelSerializer):
    class Meta:
        model = StudentProgram
        fields = "__all__"