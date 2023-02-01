from django.contrib import admin

# Register your models here.
from .models import Client , Profil , Contract , Event , UserType

@admin.register(Client , Profil , Contract , Event , UserType)

class ClientAdmin(admin.ModelAdmin):
    pass
