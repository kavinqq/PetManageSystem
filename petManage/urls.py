from django.urls import path
from petManage.views import *
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [    
    path('membersignup/', MemberSignUpView.as_view()),
    path('petcategoryinfo/', pet_category_info),
    path('addpet/', AddPet.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('test/', test_form, name = "test"),
    path('test2/', test_template, name = "test2"),
]