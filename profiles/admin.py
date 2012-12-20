from profiles.models import Profile
from django.contrib import admin

class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)
