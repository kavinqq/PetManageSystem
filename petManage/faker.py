import random
from faker import Faker
from datetime import date
from petManage.models import *

print('Faker_test mode ON!')

faker = Faker('zh-TW')
faker2 = Faker()

# 隨機暱稱產生器
def nickname_generator():

    nickname = '小'

    nickname += faker.last_name_female()

    return nickname

# 開始時間
# def get_start_date():    

#     start_date = faker.date_between(start_date = date(2000, 1, 1), end_date = date(2021, 12, 31))    

#     return start_date

# 結束時間
# def get_end_date():   

#     end_date = faker.date_between(start_date = date(2000, 1, 1))

#     return end_date

# 獲得隨機寵物id
# def get_random_pet_id():

#     max_id = Pets.objects.all().count()

#     get_id = random.randint(1, max_id)

    # return get_id

# 獲得隨機寵物tuple
# def get_random_pet():

#     max_id = Pets.objects.all().count()

#     get_id = random.randint(1, max_id)

#     return Pets.objects.get(id = get_id)


# # 產生會員假資料
# for i in range(10):
#     Members.objects.create(
#         username = faker2.name(),
#         first_name = faker.first_name(),
#         last_name = faker.last_name(),
#         birth_date = faker.date(),
#         email = faker.email(),
#         phonenumber = faker.phone_number(),
#         address = faker.address()
#     )


# 獲得隨機的member_id
# def get_random_member_id():

#     all_id = Members.objects.all().values_list("id", flat=True)

#     print('value_list data type')
#     print(type(all_id))    

#     print('all_id')
#     print(all_id)

#     index = random.randint(0, all_id.count() - 1)

#     return all_id[index]


# 產生寵物假資料
# for i in range(2):

#     newpet = Pets.objects.create(
#         name = faker2.name(),
#         nickname = nickname_generator(),        
#         species = random.randint(1, 8),
#         breed = faker.country(),
#         gender = random.randint(1, 2),
#         birth_date = faker.date(),                                                                
#         host_id = get_random_member_id()
#     )
    
#     assistants_id = get_random_member_id()

#     while assistants_id == newpet.host_id:
#         assistants_id = get_random_member_id()

#     newpet.assistants.add(get_random_member_id())


# 產生留言板假資料
# for i in range(2):
#     MessageBoard.objects.create(
#         topic = random.randint(1, 4),
#         title = faker.text(max_nb_chars = 6, ext_word_list = ['飲食', '可愛', '散步', '寵物衣服']),
#         content = faker.text(max_nb_chars = 100),        
        
#         pet_id = get_random_pet_id()
#     )



# shell執行
# exec(open("./petManage/faker.py", encoding = 'utf-8').read())


queryset1 = Members.objects.filter(first_name__contains = '婷')

print("queryset1")
print(queryset1.values_list())

queryset2 = Members.objects.filter(first_name__in = ['冠霖','雅婷'])

print("queryset2")
print(queryset2.values_list())

queryset3 = Members.objects.filter(birth_date__range = ['2000-01-01', '2022-06-10'])

print("queryset3")

for i in queryset3:
    print('\t使用者\t' + i.username + '\t出生年月日\t' + str(i.birth_date))

queryset4 = Members.objects.filter(id__lt = 5)

print("queryset4")
for i in queryset4:
    print('\t使用者id\t' + str(i.id))