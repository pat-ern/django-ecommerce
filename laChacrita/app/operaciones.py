# recibe queryset, devuelve un integer
# def calcularPromedio(dict)
def calcular_promedio(lst):
    sum = 0
    for i in lst:
        sum+=i
    avg = sum/len(lst)
    result = round(avg,1)
    return result

def contar_elementos(queryset):
    total = 0
    for i in queryset:
        total += 1
    return total