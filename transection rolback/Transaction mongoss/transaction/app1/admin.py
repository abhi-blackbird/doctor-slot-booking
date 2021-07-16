from django.contrib import admin
from .models import user_profile,user_detail
# Register your models here.
admin.site.register(user_profile)
admin.site.register(user_detail)