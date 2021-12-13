# interior design freelancer filters
from django_filters import rest_framework as filters
from dfilters.models import Journal


class BaseOrderBy(filters.FilterSet):
    order_by = filters.CharFilter(method="order_by_filter")

    def order_by_filter(self, qs, name, value):
        return qs.order_by(value)


class JournalFilter(BaseOrderBy):
    title = filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
    )
    author = filters.CharFilter(
        field_name='author',
        lookup_expr='icontains',
    )
    categories = filters.CharFilter(
        field_name='categories',
        lookup_expr='icontains',
    )
    publish_date = filters.CharFilter(
        field_name='publish_date',
        lookup_expr='icontains',
    )
    views = filters.CharFilter(
        field_name='views',
        lookup_expr='icontains',
    )

    class Meta:
        model = Journal
        fields = [
            'title',
            'author',
            'categories',
            'publish_date',
            'views',
            'reviewed',
        ]
