import json
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from petManage.forms import TestForm
from petManage.serializers import *
from petManage.models import *
from enums.CodeNMsgEnum import *
from petManage.forms import *

class MemberSignUpView(GenericAPIView):
    '''
    主人註冊表
    '''

    queryset = Members.objects.all()
    serializer_class = MembersSignUpSerializer

    def post(self, request):

        data = request.data
        serializers = self.serializer_class(data = data)

        if serializers.is_valid():
            Members.objects.create_user(**serializers.validated_data)

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



def test_form(request):

    if request.method == 'POST':
        form = TestForm(request.POST)
        
        if form.is_valid():

            return HttpResponse('Correct!')

    else:
        form = TestForm()

        context = {'form': form, 'str': "string"}

        

    return render(request, 'test1.html', context) 


# template流程練習
def test_template(request):

    test_dict4 = dict(
        test_dict = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5},

        test_dict2 = {'a' : 2, 'b' : 3, 'c' : 4, 'd' : 5, 'e' : 6},

        test_dict3 = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}
    )

    return render(request, 'test2.html', {"dics": test_dict4})
