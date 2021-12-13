from rest_framework import generics
from rest_framework import permissions, viewsets
from dfilters.api.paginations import LimitPagination
from dfilters.api.serializers import ApiFilterViewSerializers
from dfilters.models import Author, Category, Journal

from dfilters.views import filter
from dfilters.api.filter import JournalFilter


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
