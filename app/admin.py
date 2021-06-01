from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Contact

# customize contact admin menu


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'email', 'info', 'phone')
    list_editable = ('info',)
    list_per_page = 10
    search_fields = ('name', 'gender', 'email', 'info', 'phone')
    list_filter = ('gender', 'date_added')


admin.site.register(Contact, ContactAdmin)
# removing what I don't need in admin panel, 'should be imported first'
admin.site.unregister(Group)
