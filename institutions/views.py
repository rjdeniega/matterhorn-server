from rest_framework.generics import ListCreateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from core.mixins import MemorandumAdminMixin
from core.views import ModelUpdateDestroyRetrieveView
from institutions.serializers import *
from institutions.models import *
from django.contrib.auth.models import Permission
from rest_framework.response import Response


class InstitutionListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer


class InstitutionUpdateDestroyRetrieveView(ModelUpdateDestroyRetrieveView):
    permission_classes = (IsAuthenticated,)
    queryset = Institution.all_objects
    serializer_class = InstitutionSerializer


class MemorandumListCreateView(MemorandumAdminMixin):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Memorandum.objects.all()
    serializer_class = MemorandumSerializer
    lookup_field = 'institution_id'

    def get_queryset(self):
        institution = self.kwargs['institution_id']
        return super().get_queryset().filter(institution=institution)

    def perform_create(self, serializer):
        institution = Institution.objects.get(id=self.kwargs['institution_id'])
        serializer.save(institution=institution)


class MemorandumUpdateDestroyRetrieveView(MemorandumAdminMixin):
    permission_classes = (IsAuthenticated,)
    queryset = Memorandum.all_objects
    serializer_class = MemorandumSerializer


class ProgramListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


class ProgramRetrieveUpdateDestroyView(ModelUpdateDestroyRetrieveView):
    permission_classes = (IsAuthenticated,)
    queryset = Program.all_objects
    serializer_class = ProgramSerializer


class LinkageListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Linkage.objects.all()
    serializer_class = LinkageSerializer


class LinkageRetrieveUpdateDestroyView(ModelUpdateDestroyRetrieveView):
    permission_classes = (IsAuthenticated,)
    queryset = Linkage.objects.all()
    serializer_class = LinkageSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(LinkageRetrieveUpdateDestroyView, self).get_serializer(*args, **kwargs)
