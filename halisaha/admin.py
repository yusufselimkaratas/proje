from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Customer)
admin.site.register(FieldOwner)
admin.site.register(Referee)

admin.site.register(Field)
admin.site.register(Agenda)
admin.site.register(Address)

admin.site.register(Reservation)
admin.site.register(Comment)
admin.site.register(FieldConfiguration)
admin.site.register(FieldOwnerDiscount)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(Goal)
admin.site.register(PlayerSearch)