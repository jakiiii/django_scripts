from rest_framework import generics
from rest_framework import permissions, viewsets
from apps.dfilters.api.paginations import LimitPagination
from apps.dfilters.api.serializers import ApiFilterViewSerializers
from apps.dfilters.models import Author, Category, Journal

from apps.dfilters.views import filter
from apps.dfilters.api.filter import JournalFilter


class ApiFilterView(generics.ListAPIView):
    permission_classes = []
    serializer_class = ApiFilterViewSerializers
    filterset_class = JournalFilter

    def get_queryset(self):
        journal_qs = filter(self.request)
        return journal_qs


# class ApiFilterView(viewsets.ModelViewSet):
#     permission_classes = []
#     # pagination_class = LimitPagination
#     serializer_class = ApiFilterViewSerializers
#     filterset_class = JournalFilter
#
#     def get_queryset(self):
#         journal_qs = filter(self.request)
#         return journal_qs
