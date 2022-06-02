import random
from faker import Faker
from datetime import date
from petManage.models import *

faker = Faker('zh-TW')
faker2 = Faker()

# 測試 FAKER 在幹嘛
print(faker.first_name())
print(faker.last_name())
print(faker.date_time())
print(faker.date())
print(faker.email())
print(faker.address())
print(faker.text(max_nb_chars = 255))

print(faker.name())
print(faker2.name())




# 手機號碼產生器
def mobile_phone_generator():

    phone_number = '09'

    for i in range(8):
        phone_number += str(random.randint(0, 9))
    
    return phone_number

# 隨機暱稱產生器
def nickname_generator():

    nickname = '小'

    nickname += faker.last_name_female()

    return nickname

# 獲得隨機的host_id
def get_random_host_id():

    all_id = Hosts.objects.all().values_list("id", flat=True)

    index = random.randint(0, all_id.count() - 1)

    return all_id[index]

# 開始時間
def get_start_date():    

    start_date = faker.date_between(start_date = date(2000, 1, 1), end_date = date(2021, 12, 31))    

    return start_date

# 結束時間
def get_end_date():   

    end_date = faker.date_between(start_date = date(2000, 1, 1))

    return end_date

# 獲得隨機寵物id
def get_random_pet_id():

    max_id = Pets.objects.all().count()

    get_id = random.randint(1, max_id)

    return get_id

# 獲得隨機寵物tuple
def get_random_pet():

    max_id = Pets.objects.all().count()

    get_id = random.randint(1, max_id)

    return Pets.objects.get(id = get_id)


# # 產生主人假資料
# for i in range(10):
#     Hosts.objects.create(
#         first_name = faker.first_name(),
#         last_name = faker.last_name(),
#         birth_date = faker.date(),
#         email = faker.email(),
#         phonenumber = faker.phone_number(),
#         address = faker.address()
#     )


# 產生寵物假資料
for i in range(2):

    Pets.objects.create(
        name = faker2.name(),
        nickname = nickname_generator(),        
        category = random.randint(1, 7),
        type = faker.country(),
        gender = random.randint(1, 2),
        birth_date = faker.date(),                                                                
        host_id = get_random_host_id()
    )

# 產生協助飼養者假資料
for i in range(2):           

    assistant = Assistants.objects.create(
        first_name = faker.first_name(),
        last_name = faker.last_name(),
        birth_date = faker.date(),        
        email = faker.email(),
        start_time = get_start_date(),
        end_time = get_end_date(),
        phonenumber = faker.phone_number(),
        address = faker.address(),
    )

# 這兩個都可以
pet = get_random_pet()
pet_id = get_random_pet_id()

assistant.pet.add(pet_id)
assistant.pet.set([pet])

#assistant.pet.add(get_random_pet())


# # 產生留言板假資料
# for i in range(2):
#     MessageBoard.objects.create(
#         topic = random.randint(1, 4),
#         title = faker.text(max_nb_chars = 6, ext_word_list = ['飲食', '可愛', '散步', '寵物衣服']),
#         content = faker.text(max_nb_chars = 100),        
        
#         pet_id = get_random_pet_id()
#     )



# shell執行
# exec(open("./petManage/faker.py", encoding = 'utf-8').read())