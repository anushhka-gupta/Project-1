from django.contrib import admin

# Register your models here.
from .models import Feedback,Contact,User,Advisor,Service
admin.site.register(Feedback)
admin.site.register(Contact)
admin.site.register(User)
admin.site.register(Advisor)
admin.site.register(Service)