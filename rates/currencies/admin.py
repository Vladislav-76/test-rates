from currencies.models import Currency, Rate
from django.contrib import admin
from django.contrib.auth.models import Group

admin.site.register((Currency, Rate))
admin.site.unregister(Group)
