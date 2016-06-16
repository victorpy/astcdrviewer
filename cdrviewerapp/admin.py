from django.contrib import admin

# Register your models here.

from .models import Cdr,Accounts,Payments,RateGroup,Rate,RatedCdr

admin.site.register(Cdr)
admin.site.register(Accounts)
admin.site.register(Payments)
admin.site.register(RateGroup)
admin.site.register(Rate)
admin.site.register(RatedCdr)

