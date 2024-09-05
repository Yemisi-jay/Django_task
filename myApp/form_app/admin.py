from django.contrib import admin
from .models import MyModel, Profile, Feedback


# Register your models here.

class MyModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'city', 'state')


class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('user', 'text_area')


admin.site.register(MyModel, MyModelAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Feedback, FeedBackAdmin)
