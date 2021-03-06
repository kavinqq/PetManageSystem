from rest_framework import serializers
from petManage.models import *

class MembersSignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = Members
        fields = ('username', 'first_name', 'last_name', 'password','birth_date', 'email', 'phonenumber', 'address')



class AddPetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pets
        exclude = ['category', 'host_id']

# class PetSerializer(serializers.Serializer):