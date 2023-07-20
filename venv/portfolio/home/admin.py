from django.contrib import admin
from .models import *

# Register your models here.
class ServicesAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'type',
    )
admin.site.register(Services, ServicesAdmin)

class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'percentage',
    )
admin.site.register(Skill, SkillAdmin)

class PortfolioAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'type',
    )
    prepopulated_fields = {
        "slug": ("title",)
    }
admin.site.register(Portfolio, PortfolioAdmin)

class EducationAdmin(admin.ModelAdmin):
    list_display = (
        'school',
        'course',
        'start_date',
        'end_date'
    )
admin.site.register(Education, EducationAdmin)

class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        'company',
        'designation',
        'start_date',
        'end_date'
    )
admin.site.register(Experience, ExperienceAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'type',
    )
    prepopulated_fields = {
        "slug": ("title",)
    }
admin.site.register(Blog, BlogAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email'
    )
admin.site.register(Message, MessageAdmin)

class TypeAdmin(admin.ModelAdmin):
    list_display = (
        'type',
        'type',
    )
    prepopulated_fields = {
        "slug": ("type",)
    }
admin.site.register(Type, TypeAdmin)
