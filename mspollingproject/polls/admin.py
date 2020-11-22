from django.contrib import admin

# Register your models here.
from .models import Question, Choice

admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Welcome to the Pollster admin area"
'''
Question and Choice both models are showing in different link even though they both are connected to each with the help of relationship. Therefore, In django there is strategy call TabularInline.
'''
class ChoiceInline(admin.TabularInline):
  model = Choice

class QuestionAdmin(admin.ModelAdmin):
  fieldsets = [(None, {'fields': ['question_text']}),
          ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
  inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

# admin.site.register(Question)
# admin.site.register(Choice)