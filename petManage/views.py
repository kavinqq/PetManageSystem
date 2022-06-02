import json
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from petManage.serializers import *
from petManage.models import *
from enums.CodeNMsgEnum import *

class HostSignUpView(GenericAPIView):
    '''
    主人註冊表
    '''

    queryset = Hosts.objects.all()
    serializer_class = HostSignUpSerializer

    def post(self, request):

        data = request.data
        serializers = self.serializer_class(data = data)

        if serializers.is_valid():
            Hosts.objects.create_user(**serializers.validated_data)

            return Response(CodeNMsgEnum.HOST_SIGN_UP_SUCCESS.get_dict())
        else:
            return Response(CodeNMsgEnum.HOST_SIGN_UP_FAIL.get_dict())
    

@method_decorator(login_required, name = 'post')
class AddPet(GenericAPIView):
    '''
    主人新增寵物
    '''

    queryset = Pets.objects.all()
    serializer_class = AddPetSerializer        

    def post(self, request, category_option):        

        data = request.data

        print(type(data))
        
        serializers = self.serializer_class(data = data)

        if serializers.is_valid():            
            pet = Pets.objects.create(**serializers.validatedr_data)

            pet.category = category_option

            pet.host_id = request.user.id

            return Response(CodeNMsgEnum.PET_ADD_SUCCESS.get_dict())
        else:
            return Response(CodeNMsgEnum.PET_ADD_FAIL.get_dict())
            

def pet_category_info(self):
    '''
    回傳一個可供選擇的寵物類別的字典
    '''
    pet_choice_list = Pets.category.field.choices

    result = dict(pet_choice_list)    

    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json")