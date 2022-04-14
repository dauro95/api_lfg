from django.contrib import admin
from .models import Party_user, Videogame,Party,Message,apiModel

admin.site.register(Videogame)
admin.site.register(Party)
admin.site.register(Message)
admin.site.register(Party_user)

# Register your models here.
