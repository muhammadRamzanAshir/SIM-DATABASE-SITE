from django.contrib import admin
from .models import *
from django.utils.html import format_html

class NavbarItemAdmin(admin.ModelAdmin):
    list_display     = ['name','parent','is_active']
    list_filter      = ['is_active']
    search_fields    = ['name']


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title','button_text', 'button_link')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display    = ("title", "icon_class","order_number", "service_heading","service_subheading")
    list_editable   = ("icon_class","order_number","service_heading","service_subheading")

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name']

class AboutUsAdmin(admin.ModelAdmin):
    list_display    = ("title","subtitle")
    search_fields   = ("title", "subtitle")
    list_editable   = ("subtitle")

@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ("title", "plan_type", "price")
    list_filter = ("plan_type",)


class PhoneDetailAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'father_name', 'cnic', 'address', 'created_at')  # Display fields in the admin panel
    search_fields = ('number', 'name', 'cnic', 'father_name')  # Enable search functionality
    list_filter = ('created_at',)  # Filter records by creation date

admin.site.register(PhoneDetail, PhoneDetailAdmin)
admin.site.register(SupportInfo)
admin.site.register(AboutUs)
admin.site.register(NavbarItem, NavbarItemAdmin)
admin.site.register(SectionTitle)
admin.site.register(Footer)