import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class Hosts(AbstractUser):
    '''
    主人資料表
    '''
    
    username = models.CharField(max_length = 150, unique = True)
    first_name = models.CharField(max_length = 12, verbose_name = "名字")    
    last_name = models.CharField(max_length = 8, verbose_name = "姓氏")
    birth_date = models.DateField(blank = True, null = True, verbose_name = "出生年月日")
    email = models.EmailField(max_length = 255, verbose_name = "電子信箱")
    phonenumber = models.CharField(max_length = 10, verbose_name = "聯絡號碼")
    address = models.CharField(max_length = 80, verbose_name = "地址")
    

    class Meta:
        verbose_name_plural = "寵物主人"        
        db_table = '主人資料'


class Pets(models.Model):
    '''
    寵物資料表
    '''

    # 性別選項
    GENDER_CHOICES = (
        (1, 'Male'),
        (2, 'Female'),
    )

    # 種類選項
    SPECICS_CHOICES = (
        (1, '狗'),
        (2, '貓'),
        (3, '青蛙'),
        (4, '鴨子'),
        (5, '老鼠'),
        (6, '魚'),
        (7, '鳥類'),
        (8, '其他')
    )    
    
    name = models.CharField(max_length = 100, verbose_name = "姓名")
    nickname = models.CharField(max_length = 10, blank = True, verbose_name = "暱稱")
    species = models.IntegerField(choices = SPECICS_CHOICES, verbose_name = "種類")
    breed = models.CharField(max_length = 22, verbose_name = "品種")
    gender = models.IntegerField(choices = GENDER_CHOICES, verbose_name = "性別")
    birth_date = models.DateField(verbose_name = "出生年月日")        

    host = models.ForeignKey(Hosts, on_delete = models.CASCADE, verbose_name = "主人", related_name = 'my_host')
    assistants = models.ManyToManyField(Hosts, through = "pet_and_assistants", through_fields = ('pet', 'assistant'), on_delete = models.CASCADE, verbose_name = "協助飼養者", related_name = 'my_assistants')

    class Meta:
        verbose_name_plural = "寵物"        
        db_table = '寵物資料'


class pet_and_assistants(models.Model):
    '''
    寵物和協助飼養者的多對多關聯表
    '''

    pet = models.ForeignKey(Pets, on_delete = models.CASCADE, verbose_name = "寵物")    
    assistant = models.ForeignKey(Hosts, on_delete = models.CASCADE,verbose_name = "協助飼養者")    
    start_date = models.DateField(verbose_name = "開始協助日期")
    end_date = models.DateField(verbose_name = "結束協助日期")

    class Meta:
        db_table = '寵物和協助飼養者關聯表'



class PetRecords(models.Model):
    '''
    寵物日常紀錄表
    '''
    # 身體狀況
    STATUS_CHOICES = (
        (1, '健康'),
        (2, '不舒服'),        
    )

    # 治療狀況
    HEAL_STATUS_CHOICES = (
        (1, '症狀改善'),
        (2, '症狀無改變'),
        (3, '症狀加劇')
    )

    date = models.DateField(default = datetime.date.today, verbose_name = "填表日期")      
    number_of_excretion =  models.IntegerField(null = True, blank = True, verbose_name = "當日排泄次數")
    number_of_meals = models.IntegerField(null = True, blank = True, verbose_name = "當日用餐次數")
    weight = models.IntegerField(null = True, blank= True, verbose_name = "寵物體重")
    status = models.IntegerField(choices = STATUS_CHOICES, verbose_name = "身體狀況")            
    photos = models.ImageField(upload_to = "%Y/%m/%d/", verbose_name = "日常照")
    
    hospital_name = models.CharField(max_length = 22, blank = True, verbose_name = "醫院/診所的名稱")    
    diseases = models.CharField(max_length = 255, blank = True, verbose_name = "症狀或病名")
    heal_status = models.IntegerField(choices = HEAL_STATUS_CHOICES, blank = True, null = True, verbose_name = "治療後狀況")
    notes = models.TextField(blank = True, verbose_name = "備註:")  


    pet = models.ForeignKey(Pets, on_delete = models.CASCADE, verbose_name = "該紀錄寵物")
    
    class Meta:        
        verbose_name_plural = "寵物紀錄"        
        db_table = '寵物紀錄'
        unique_together = ("date", "pet")


# class Assistants(models.Model):
#     '''
#     協助飼養者
#     '''
    
#     first_name = models.CharField(max_length = 12, verbose_name = "名字")    
#     last_name = models.CharField(max_length = 8, verbose_name = "姓氏")
#     birth_date = models.DateField(verbose_name = "出生年月日")
#     email = models.EmailField(max_length = 255, verbose_name = "電子信箱")
#     phonenumber = models.CharField(max_length = 10, verbose_name = "聯絡號碼")
#     start_time = models.DateField(verbose_name = "開始日期")
#     end_time = models.DateField(verbose_name = "結束日期")
#     address = models.CharField(max_length = 80, verbose_name = "地址")

#     pet = models.ManyToManyField(Pets)

#     class Meta:
#         verbose_name_plural = "協助飼養寵物者"        
#         db_table = '協助飼養寵物者'


class MessageBoard(models.Model):
    '''
    留言板
    '''
    
    TOPIC_CHOICES = (
        (1, '閒聊'),
        (2, '寵物飲食'),
        (3, '寵物生病'),                        
        (4, '其他')
    )    

    topic = models.IntegerField(choices = TOPIC_CHOICES, verbose_name = "主題")    
    title = models.CharField(max_length = 50, verbose_name = "標題")
    content = models.TextField(verbose_name = "留言內容")
    pet = models.ForeignKey(Pets, on_delete = models.DO_NOTHING, verbose_name = "該紀錄的寵物")

    class Meta:
        verbose_name_plural = "留言板"        
        db_table = '留言板'