from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, mixins, permissions
from .serializers import TaskSerializer
from ..models import Task


# class TaskImageUpload(ModelViewSet):
#     serializer_class = TaskSerializer
#     queryset = Task.objects.all()


class TaskImageUpload(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
