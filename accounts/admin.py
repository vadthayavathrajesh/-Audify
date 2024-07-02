from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Video)
admin.site.register(Comments)
admin.site.register(Customer)
admin.site.register(VideoLinks)
admin.site.register(CommentLinks)
admin.site.register(FBVideoLinks)
admin.site.register(FBCommentLinks)
admin.site.register(TWVideoLinks)
admin.site.register(TWCommentLinks)