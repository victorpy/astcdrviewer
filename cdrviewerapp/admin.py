from django.contrib import admin

# Register your models here.

from .models import Cdr,Accounts,Payments,RateGroup,Rate,RatedCdr

class CdrAdmin(admin.ModelAdmin):
	#fields = ['acctid','calldate', 'disposition', 'accountcode' ]
	list_display = ('acctid','src','dst' ,'calldate', 'disposition', 'accountcode')
	#list_filter = ['acctid']

class RatedCdrAdmin(admin.ModelAdmin):
	list_display = ('calldate','clid','dst', 'accountcode')

class AccountsAdmin(admin.ModelAdmin):
        list_display = ('account_code','username','credit')


admin.site.register(Cdr,CdrAdmin)
admin.site.register(Accounts, AccountsAdmin)
admin.site.register(Payments)
admin.site.register(RateGroup)
admin.site.register(Rate)
admin.site.register(RatedCdr, RatedCdrAdmin)

