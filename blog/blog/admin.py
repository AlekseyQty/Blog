from django.contrib import admin
from .models import Post
# Register your models here.


def hide(modeladmin, request, queryset):
    queryset.update(is_hidden='True')


def show(modeladmin, request, queryset):
    queryset.update(is_hidden='False')


hide.short_description = "Hide post"
show.short_description = "Show post"


class PostAdmin(admin.ModelAdmin):
    actions = [hide, show]


admin.site.register(Post, PostAdmin)