from django.contrib import admin
from authentification.models import User 
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Association)
admin.site.register(PhysicalUser)
admin.site.register(Annonce)
admin.site.register(Cagniote)
admin.site.register(Benevole)
admin.site.register(Notification)
