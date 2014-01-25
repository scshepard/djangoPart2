from django.contrib import admin
from polls.models import Poll

class PollAdmin(admin.ModelAdmin):
	fields = ['pub_date','question']
	
# Register your models here.
admin.site.register(Poll, PollAdmin)
