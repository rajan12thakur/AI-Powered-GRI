

# Register your models here.

from django.contrib import admin

# importing only those models which we want to register/show in the admin panel
from .models import UserAccount, Role

admin.site.register(UserAccount)
admin.site.register(Role)
