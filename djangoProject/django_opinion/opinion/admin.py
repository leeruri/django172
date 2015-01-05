from django.contrib import admin
from opinion.models import Opinion
from opinion.models import OpinionUser

class OpinionAdmin(admin.ModelAdmin):
    fields = ['opinion_title', 'opinion_contents', 'opinion_writer_id', 'opinion_link_id', 'ip_address', 'reg_date']

'''
fieldsets = [
(None,               {'fields': ['question_text']}),
('Date information', {'fields': ['pub_date']}),
]
'''

admin.site.register(Opinion, OpinionAdmin)
admin.site.register(OpinionUser)