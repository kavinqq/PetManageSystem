import datetime
from unicodedata import category
from django.db import models
from django.dispatch import receiver

class Hosts(models.Model):
    '''
    主人資料表
    '''

    id = models.AutoField(max_length = 10, primary_key = True, verbose_name = "UID")
    first_name = models.CharField(max_length = 100, verbose_name = "名字")    
    last_name = models.CharField(max_length = 50, verbose_name = "姓氏")
    age = models.IntegerField(blank = True, null = True, verbose_name = "年齡")
    email = models.EmailField(max_length = 255, verbose_name = "電子信箱")
    phonenumber = models.IntegerField(max_length = 10, verbose_name = "手機號碼")


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

    id = models.AutoField(primary_key = True, verbose_name = "UID")
    name = models.CharField(max_length = 100, verbose_name = "姓名")
    nickname = models.CharField(max_length = 100, null = True, blank = True, verbose_name = "暱稱")
    category = models.IntegerField(max_length = 1, choices = CATEGORY_CHOICES)
    type = models.CharField(max_length = 10)
    gender = models.IntegerField(choices = GENDER_CHOICES, verbose_name = "性別")
    birth_date = models.DateField(verbose_name = "出生年月日")    
    weight = models.IntegerField(verbose_name = "體重")

    host_id = models.ForeignKey(Hosts, verbose_name = "主人的UID")


class DailyRecords(models.Model):
    '''
    寵物日常紀錄表
    '''

    date = models.DateField(default = datetime.date.today, verbose_name = "填表日期")  #預設今天     
    number_of_excretion =  models.IntegerField(default = 2, verbose_name = "當日排泄次數")
    number_of_meals = models.IntegerField(default = 2, verbose_name = "當日用餐次數")


    pet_id = models.ForeignKey(Pets, on_delete = models.CASCADE, verbose_name = "該紀錄寵物的UID")
    
    class Meta:
        unique_together = ("date", "pet_id")



class PetDiscomfortRecords(models.Model):
    '''
    寵物不舒服紀錄
    '''

    date = models.DateField(default = datetime.date.today, verbose_name = "填表日期")  #預設今天
    symptom = models.TextField(max_length = 500, verbose_name = "不舒服的症狀")

    pet_id = models.ForeignKey(Pets, on_delete = models.CASCADE, verbose_name = "該紀錄寵物的UID")

    class Meta:
        unique_together = ("date", "pet_id")
    

class PetRecoverRecords(models.Model):
    '''
    寵物康復紀錄
    '''

    date = models.DateField(default = datetime.date.today, verbose_name = "填表日期")  #預設今天  
    clinic_name = models.CharField(max_length = 100, verbose_name = "最後就醫診所名稱")

    pet_id = models.ForeignKey(Pets, on_delete = models.CASCADE, verbose_name = "該紀錄寵物的UID")

    class Meta:
        unique_together = ("date", "pet_id")


class Assistants(models.Model):
    '''
    協助飼養者
    '''

    id = models.AutoField(max_length = 10, primary_key = True, verbose_name = "UID")
    first_name = models.CharField(max_length = 100, verbose_name = "名字")    
    last_name = models.CharField(max_length = 50, verbose_name = "姓氏")
    age = models.IntegerField(blank = True, null = True, verbose_name = "年齡")
    email = models.EmailField(max_length = 255, verbose_name = "電子信箱")
    phonenumber = models.IntegerField(max_length = 10, verbose_name = "手機號碼")



class PetsAndAssistants(models.Model):
    '''
    寵物和協助飼養者的關聯
    '''
    pet_id = models.ForeignKey(Pets, verbose_name = "寵物UID")
    assistant_id = models.ForeignKey(Assistants, verbose_name = "協助飼養者UID")

    class Meta:    
        unique_together = ("pet_id", "assistant_id") #聯合主鍵


class MessageBoard(models.Model):
    '''
    留言板
    '''

    id = models.AutoField(primary_key = True, verbose_name = "該則留言ID")
    poster = models.IntegerField(verbose_name = "發文者")
    receiver = models.IntegerField(verbose_name = "受文者")
    text = models.TextField(max_length = 500, verbose_name = "留言內容")

    pet_id = models.ForeignKey(Pets, verbose_name = "該紀錄寵物的UID")