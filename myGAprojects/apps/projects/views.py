from django_filters import rest_framework as filters
from rest_framework import generics, viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from .models import Project, ProjectFilter
from .serializers import ProjectSerializer

from django_filters.rest_framework import DjangoFilterBackend


class AllProjectViews(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ByProjectTypeView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        serializer.save()


class ProjectFilterView(generics.ListAPIView):
    queryset = Project.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_class = ProjectFilter
    serializer_class = ProjectSerializer



# class ProjectFilterViewSet(viewsets.ModelViewSet):
#     __basic_fields = ('category')
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer(queryset, many=True)
#     filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
#     filter_fields = __basic_fields
#     search_fields = __basic_fields




# class AllProjectViews(generics.ListAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer
#
#
# class ByProjectTypeView(viewsets.ViewSet):
#     filter_backends = (filters.DjangoFilterBackend,)
#     filter_fields = ("category",)
#
#     def get_queryset(self):
#         queryset = Project.objects.filter(category=self.request.category)
#         return queryset
#     serializer_class = ProjectSerializer
#
#     def perform_create(self, serializer):
#         serializer.save()
#

# def get_queryset(self):
#     queryset = Project.objects.filter(category=self.request.category)
#     return queryset
# serializer_class = ProjectSerializer
