from django.contrib import admin
from .models import MyModel, Profile


# Register your models here.

class MyModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'city', 'state')


admin.site.register(MyModel, MyModelAdmin)
admin.site.register(Profile, ProfileAdmin)
