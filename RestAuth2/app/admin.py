from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import GameUser

admin.site.register(GameUser, UserAdmin)