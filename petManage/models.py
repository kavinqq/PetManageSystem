import datetime
from django.db import models

class Hosts(models.Model):
    '''
    主人資料表
    '''

    first_name = models.CharField(max_length = 12, verbose_name = "名字")    
    last_name = models.CharField(max_length = 8, verbose_name = "姓氏")
    birth_date = models.DateField(verbose_name = "出生年月日")
    email = models.EmailField(max_length = 255, verbose_name = "電子信箱")
    phonenumber = models.IntegerField(max_length = 10, verbose_name = "手機號碼")
    address = models.CharField(max_length = 80, verbose_name = "地址")

    class Meta:
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
    CATEGORY_CHOICES = (
        (1, 'Dog'),
        (2, 'Cat'),
        (3, 'Snake'),
        (4, 'Spider'),
        (5, 'Fog'),
        (6, 'Duck'),
        (7, 'Chicken')    
    )    
    
    name = models.CharField(max_length = 20, verbose_name = "姓名")
    nickname = models.CharField(max_length = 10, null = True, blank = True, verbose_name = "暱稱")
    category = models.IntegerField(max_length = 1, choices = CATEGORY_CHOICES, verbose_name = "種類")
    type = models.CharField(max_length = 22, verbose_name = "品種")
    gender = models.IntegerField(choices = GENDER_CHOICES, verbose_name = "性別")
    birth_date = models.DateField(verbose_name = "出生年月日")        

    host = models.ForeignKey(Hosts, verbose_name = "主人的UID")

    class Meta:
        db_table = '寵物資料'


class DailyRecords(models.Model):
    '''
    寵物日常紀錄表
    '''

    STATUS_CHOICES = (
        (1, '健康'),
        (2, '不舒服'),
        (3, '治療中')        
    )

    date = models.DateField(default = datetime.date.today, verbose_name = "填表日期")      
    number_of_excretion =  models.IntegerField(verbose_name = "當日排泄次數")
    number_of_meals = models.IntegerField(verbose_name = "當日用餐次數")
    weight = models.IntegerField(null = True, blank= True, verbose_name = "寵物體重")
    status = models.TextField(choices = STATUS_CHOICES, verbose_name = "身體狀況")
    notes = models.TextField(verbose_name = "日常記錄")

    pet = models.ForeignKey(Pets, on_delete = models.CASCADE, verbose_name = "該紀錄寵物")
    
    class Meta:
        class Meta:
            db_table = '寵物日常紀錄表',
            unique_together = ("date", "pet")


class PetRecoveryRecords(models.Model):
    '''
    寵物治療後紀錄表
    '''        

    STATUS_CHOICES = (
        (1, '症狀改善')
        (2, '症狀無改變')
        (3, '症狀加劇')
    )

    date = models.DateField(default = datetime.date.today, verbose_name = "填表日期")  
    number_of_excretion =  models.IntegerField(verbose_name = "當日排泄次數")
    number_of_meals = models.IntegerField(verbose_name = "當日用餐次數")      
    hospital_name = models.CharField(max_length = 22, verbose_name = "醫院/診所的名稱")
    status = models.IntegerField(choices = STATUS_CHOICES, verbose_name = "治療後狀況")
    diseases = models.CharField(max_length = 255, verbose_name = "症狀或病名")
    notes = models.TextField(verbose_name = "注意事項")        

    pet = models.ForeignKey(Pets, on_delete = models.CASCADE, verbose_name = "該紀錄寵物")

    class Meta:
        db_table = '寵物日常紀錄表',
        unique_together = ("date", "pet")


class Assistants(models.Model):
    '''
    協助飼養者
    '''
    
    first_name = models.CharField(max_length = 12, verbose_name = "名字")    
    last_name = models.CharField(max_length = 8, verbose_name = "姓氏")
    birth_date = models.DateField(verbose_name = "出生年月日")
    email = models.EmailField(max_length = 255, verbose_name = "電子信箱")
    phonenumber = models.IntegerField(max_length = 10, verbose_name = "手機號碼")
    start_time = models.DateField(verbose_name = "開始日期")
    end_time = models.DateField(verbose_name = "結束日期")
    address = models.CharField(max_length = 80, verbose_name = "地址")

    pet = models.ManyToManyField(Pets, through = "PetsAndAssistants", through_fields = ('pet', 'assistant'))

    class Meta:
        db_table = '協助飼養者'


class MessageBoard(models.Model):
    '''
    留言板
    '''
    
    TOPIC_CHOICES = (
        (1, '閒聊'),
        (2, '飲食'),
        (3, '生病'),                
        (4, '配對'),
        (5, '認養'),
        (6, '其他')
    )    

    topic = models.IntegerField(choices = TOPIC_CHOICES, verbose_name = "主題")    
    title = models.CharField(max_length = 50, verbose_name = "標題")
    content = models.TextField(verbose_name = "留言內容")
    pet = models.ForeignKey(Pets, verbose_name = "該紀錄的寵物")

    class Meta:
        db_table = '留言板'