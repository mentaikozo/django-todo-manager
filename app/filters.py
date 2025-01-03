from django_filters import filters
from django_filters import FilterSet
from .models import Task


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'


class TaskFilter(FilterSet):

    name = filters.CharFilter(label='タスク名', lookup_expr='contains')
    memo = filters.CharFilter(label='メモ', lookup_expr='contains')

    order_by = MyOrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('name', 'name'),
            ('notes', 'notes'),
        ),
        field_labels={
            'name': 'タスク名',
            'notes': 'メモ',
        },
        label='並び順'
    )

    class Meta:

        model = Task
        fields = ('name', 'status', 'priority', 'pub_date', 'notes')
