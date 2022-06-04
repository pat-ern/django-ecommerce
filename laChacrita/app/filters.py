import django_filters
from .models import Producto

class IndexFilter(django_filters.FilterSet):

    CHOICES = (
        ('ascending', 'Ascendente'),
        ('descending', 'Descendente')
    )

    ordering = django_filters.ChoiceFilter(label='Ordenar por precio', choices=CHOICES, method='filter_by_order')

    class Meta:
        model = Producto
        fields = {
            'nombre':['icontains'],
            'categoria':['exact'],
            'precio':['lt','gt'],
        }

    def filter_by_order(self, queryset, name, value):
        expression = 'precio' if value == 'ascending' else '-precio'
        return queryset.order_by(expression)

'''    def __init__(self, data, *args, **kwargs):
        data = data.copy()
        data.setdefault('nombre', '')
        data.setdefault('categoria', '')
        data.setdefault('precio', '')
        super().__init__(data, *args, **kwargs)'''