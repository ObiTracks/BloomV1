from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from account.models import Account

class AccountAdmin(UserAdmin):
    ordering = ()
    list_display = ('email','first_name','last_name','apt','is_admin','is_staff')
    search_fields = ('email','first_name','last_name','apt')
    readonly_fields = ('date_joined','last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)