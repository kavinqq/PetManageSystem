from django.contrib import admin
from .models import *

admin.site.register(Members)
admin.site.register(Pets)
admin.site.register(MessageBoard)
admin.site.register(PetRecords)