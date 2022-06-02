from unicodedata import category
from petManage.models import *
from django.db.models import Avg, Max, Min, Sum, Count

test1 = Pets.objects.values()
test2 = Pets.objects.values_list()

for i in test1:
    print (type(i))

print(test1)

print("--------------------")

for i in test2:
    print (type(i))

print(test2)

test3 = Pets.objects.aggregate(Avg('category'))
test4 = Pets.objects.all().aggregate(Avg('category'))

print(test3)
print(type(test3))
print(test4)

test5 = Pets.objects.aggregate(category = Count('category'))

print(test5)
print(type(test5))

test6 = Pets.objects.aggregate(sum_category = Sum('category'), max_host_id = Max('host_id'))

print(test6)
print(type(test6))
print(test6['max_host_id'])

test7 = Assistants.objects.annotate(max_id = Max('id'))

print(test7)

test8 = Assistants.objects.filter(first_name__contains = '山')

for i in test8:
    print(i.first_name + '\t' + i.address)

test9 = Assistants.objects.filter(birth_date__year = '1997')

陪毛毛



