from django.contrib import admin

from read.models import Categories, Manga, Types


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name',)}
  
@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name',)}

@admin.register(Types)
class TypesAdmin(admin.ModelAdmin):
  pass