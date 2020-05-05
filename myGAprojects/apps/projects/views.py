from rest_framework import generics, viewsets
from .models import Project
from .serializers import ProjectSerializer

class AllProjectViews(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ByProjectTypeView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        serializer.save()

# class AllProjectViews(viewsets.ModelViewSet):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer
#
#
# class ByProjectTypeView(viewsets.ModelViewSet):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer
#     lookup_field = str('category')
#
#     def perform_create(self, serializer):
#         serializer.save()
