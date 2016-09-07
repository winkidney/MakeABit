from django.contrib import admin
from words.models import Tag, Type, Word


to_register = (
    Tag,
    Type,
)


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'ctime')
    readonly_fields = ('author', )

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


admin.site.register(to_register)