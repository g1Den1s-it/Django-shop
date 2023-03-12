from django.contrib import admin

from store.models import Category, Subcategory, Goods
# Register your models here.


class ClassAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, ClassAdmin)
admin.site.register(Subcategory, ClassAdmin)
admin.site.register(Goods)