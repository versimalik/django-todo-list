from django.contrib import admin
from .models import Todo
from django.utils.html import mark_safe

# Register your models here.

admin.site.site_header = "Django  Todolist"
admin.site.site_title = "Todolist Administration"
admin.site.index_title = "Todolist Administration"
# admin.site.site_url = None

class TodoAdmin(admin.ModelAdmin):

    actions = ["set_to_done", "set_to_not_done"]

    @admin.action(description="Set selected todos to Done")
    def set_to_done(modeladmin, request, queryset):
        queryset.update(status=True)

    @admin.action(description="Set selected todos to Not Done")
    def set_to_not_done(modeladmin, request, queryset):
        queryset.update(status=False)

    def done(self, obj):
        if obj.status:
            return mark_safe("<span style=\"background-color: cyan; padding:3px\">Done</span>")
        else:
            return mark_safe("<span style=\"background-color: red; color: white; padding:3px\">Not Done</span>")

    list_display=[
        'text',
        'due_date',
        'done',
        'user',
    ]

    exclude=['user',]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Todo, TodoAdmin)