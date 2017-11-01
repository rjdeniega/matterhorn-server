from .models import *
from rest_framework.serializers import ModelSerializer


class InstitutionSerializer(ModelSerializer):
    class Meta:
        model = Institution
        fields = "__all__"


class MemorandumSerializer(ModelSerializer):
    class Meta:
        model = Memorandum
        fields = "__all__"


class ProgramSerializer(ModelSerializer):
    class Meta:
        model = Program
        fields = "__all__"


class ProgramOfferingSerializer(ModelSerializer):
    class Meta:
        model = ProgramOffering
        fields = "__all__"
