from django.contrib import admin

from curatorapp.models import Bible, Permanent, Special

# Register your models here.
admin.site.register(Permanent)
admin.site.register(Bible)
admin.site.register(Special)