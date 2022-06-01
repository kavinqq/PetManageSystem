from django.contrib import admin
from .models import *

admin.site.register(Hosts)
admin.site.register(Pets)
admin.site.register(Assistants)
admin.site.register(MessageBoard)
admin.site.register(PetRecords)