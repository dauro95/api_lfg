from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib import admin

# Create your models here.
class apiModel(models.Model):    
    def has_add_permission(request) -> bool:
        return True

    def has_change_permission(request, obj=None) -> bool:
        return False

    def has_delete_permission(request, obj=None) -> bool:
        return False


class Videogame(apiModel):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    release_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.name

class Party(apiModel):
    name = models.CharField(max_length=200)
    videogame_origin = models.ForeignKey(Videogame, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.name


class Party_user(apiModel):
    party_id = models.ForeignKey(Party, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.start_date


class Message(apiModel):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    deleted = models.BooleanField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    def has_change_permission(request, obj=None) -> bool:
        if not obj: return False

        return settings.AUTH_USER_MODEL == obj.creator

    def has_delete_permission(request, obj=None) -> bool:
        if not obj: return False

        return settings.AUTH_USER_MODEL == obj.creator

    def __str__(self) -> str:
        return self.content

