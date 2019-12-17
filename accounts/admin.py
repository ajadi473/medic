from django.contrib import admin
from .models import accounts_patientmodel,accounts_doctorsmodel

# Register your models here.


# patients model
admin.site.register(accounts_patientmodel)

# medical practitioners model
admin.site.register(accounts_doctorsmodel)