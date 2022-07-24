from django.contrib import admin
from store.models.customer import UserProfile
# Register your models here.
from django.contrib.sites.models import Site


class SiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'domain', 'name')


admin.site.unregister(Site)
admin.site.register(Site, SiteAdmin)
admin.site.register(UserProfile)
