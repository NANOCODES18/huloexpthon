from django.contrib import admin

from userdashboard.models import Profile, Referral, Verification

# Register your models here.
admin.site.register(Profile)
admin.site.register(Verification)
admin.site.register(Referral)