from GGH.models import Membership,Equipment, Post
from django.contrib import admin
#from .models import Equipment, Membership
# Register your models here.
# admin.site.register(Washirika)
@admin.register(Membership)


class MembershipAdmin(admin.ModelAdmin):
    list_display = ['full_name','phone_number', 'physical_address','gender','baptised','rescued_ggh']

@admin.register(Equipment)

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['camera', 'keyboards', 'computer', 'drums', 'guitars','speakers', 'microphones'
    ,'chairs', 'tables', 'stools']

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display=['header_image']

