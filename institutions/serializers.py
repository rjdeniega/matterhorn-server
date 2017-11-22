from django.http import Http404, request
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.utils import model_meta

from .models import *
from rest_framework.serializers import ModelSerializer, Serializer, BaseSerializer
from rest_framework import serializers


class InstitutionSerializer(ModelSerializer):
    class Meta:
        model = Institution
        fields = "__all__"


class MemorandumSerializer(ModelSerializer):
    linkages = PrimaryKeyRelatedField(many=True, queryset=Linkage.objects.all())

    class Meta:
        model = Memorandum
        exclude = ('institution',)


class LinkageSerializer(ModelSerializer):
    class Meta:
        model = Linkage


class TermSerializer(ModelSerializer):
    class Meta:
        model = Term
        exclude = ('academic_year',)


class AcademicYearSerializer(Serializer):
    academic_year_start = serializers.IntegerField()
    terms = TermSerializer(many=True)

    def validate_academic_year_start(self, value):
        if AcademicYear.objects.filter(pk=value):
            raise ValidationError("Academic Year exists")
        else:
            return value

    def validate_terms(self, value):
        term_serializer = TermSerializer(data=value)
        if term_serializer.is_valid() is False:
            raise ValidationError("All fields for term must have values!")

        return value

    def create(self, validated_data):
        terms = validated_data.pop('terms')
        instance = AcademicYear.objects.create(**validated_data)

        for term in terms:
            Term.objects.create(academic_year=instance, **term)

        return instance


class ProgramSerializer(ModelSerializer):
    terms_available = TermSerializer(many=True, read_only=True)

    class Meta:
        model = Program
        fields = "__all__"

class InboundProgramSerializer(Serializer):
    linkage = serializers.PrimaryKeyRelatedField(queryset=Linkage.objects.all())
    terms_available = serializers.PrimaryKeyRelatedField(many=True,queryset=Term.objects.all())
    academic_year = serializers.PrimaryKeyRelatedField(queryset=AcademicYear.objects.all())
    name = serializers.CharField()
    is_graduate = serializers.BooleanField()

    @staticmethod
    def convert_data(validated_data):
        return {
            "linkage": validated_data["linkage"].pk,
            "academic_year": validated_data["academic_year"].pk,
            "terms_available": [item.pk for item in validated_data["terms_available"]],
            "name": validated_data["name"],
            "is_graduate": validated_data["is_graduate"]
        }

    def create(self, validated_data):
        program_details = self.convert_data(validated_data)
        program_serializer = ProgramSerializer(data=program_details)
        if not program_serializer.is_valid():
            raise ValidationError(program_serializer.errors)
        print(validated_data)
        program = Program.objects.create(**validated_data)
        inbound_program = InboundProgram.objects.create(program=program)

        return inbound_program


class OutboundProgramSerializer(ModelSerializer):
    requirement_deadline = DateField()
    institution = PrimaryKeyRelatedField(queryset=Institution.objects.all())

    class Meta:
        model = Program
        fields = "__all__"

    def validate_extra_fields(self,value):
        if self.requirement_deadline is None:
            raise ValidationError("deadline is required")
        elif self.insitution is None:
            raise ValidationError

    def create(self, validated_data):
        instance = Program.objects.create(**validated_data)
        outbound_program = OutboundProgram.objects.create(program=instance)
        outbound_program.institution = validated_data["institution"]
        outbound_program.requirement_deadline = validated_data["requirement_deadline"]
        outbound_program.save()
        return outbound_program











