from django.urls import path
from petManage.views import *

urlpatterns = [    
    path('hostsignup/', HostSignUpView.as_view()),
    path('petcategoryinfo/', pet_category_info),
    path('addpet/', AddPet.as_view())
]