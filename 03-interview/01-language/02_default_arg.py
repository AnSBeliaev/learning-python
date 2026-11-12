# Пустой список в значении по умолчанию создаётся один раз, в момент объявления
# функции, а не при каждом вызове. Все вызовы без своего списка получают один
# и тот же список, поэтому элементы копятся.
#
# Безопасная замена: по умолчанию передать None. None не меняется.
# Если аргумент не передали, внутри функции создать новый пустой список.

def f_shared(x, items=[]):
    items.append(x)
    return items

print(f_shared(1))
print(f_shared(2))

def f_safe(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items

print(f_safe(1))
print(f_safe(2))
