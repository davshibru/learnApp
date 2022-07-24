from django.contrib import admin
from .models import Geniral_Topics, Topics, UserAccess, Lections, UserResults

class GeniralTopicsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class LectionTopicsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class TopicsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"english_name": ("name",)}

admin.site.register(Geniral_Topics, GeniralTopicsAdmin)
admin.site.register(Topics, TopicsAdmin)
admin.site.register(UserAccess)
admin.site.register(Lections)
admin.site.register(UserResults)
