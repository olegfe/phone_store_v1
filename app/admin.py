from django.contrib import admin

from app.models import Comment, Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ['email','date',]

admin.site.register(Contact,ContactAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['author','post','date']


admin.site.register(Comment,CommentAdmin)