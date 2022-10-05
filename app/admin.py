from django.contrib import admin
from .models import Profile

# this is to register/add the table into the admin panel
admin.site.register(Profile)
