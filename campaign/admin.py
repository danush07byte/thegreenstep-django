from django.contrib import admin
from .models import Volunteer

admin.site.site_header = "The Green Step Admin Panel"
admin.site.site_title = "SDG 13 Admin"
admin.site.index_title = "Climate Action Volunteer Management"

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'interest')
    search_fields = ('name', 'email', 'interest')
    list_filter = ('interest',)
    ordering = ('name',)