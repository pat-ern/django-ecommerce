import django_filters
from .models import Snippet

class SnippetFilter(django_filters.FilterSet):

    CHOICES = (
        ('ascending', 'Ascendente'),
        ('descending', 'Descendente')
    )

    ordering = django_filters.ChoiceFilter(label='Ordering', choices=CHOICES, method='filter_by_order')

    class Meta:
        model = Snippet
        fields = {
            'title':['icontains'],
            'body':['icontains'],
        }

    def filter_by_order(self, queryset, name, value):
        expression = 'created' if value == 'ascending' else '-created'
        return queryset.order_by(expression)