from django.contrib import admin

from django.contrib import admin
from .models import (
    WebsiteSettings,
    HomeSection,
    AboutSection,
    ProductCategory,
    Product,
    Feature,
    ContactSettings,
    ContactEnquiry,
    ConnectSection,
    NavigationLink,
    FooterSettings,
)


admin.site.site_header = "Synexta Pharma Administration"
admin.site.site_title = "Synexta Pharma Admin"
admin.site.index_title = "Website Content Management"


@admin.register(WebsiteSettings)
class WebsiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("site_name",)


@admin.register(HomeSection)
class HomeSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "button_text")
    search_fields = ("title",)


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "is_active", "display_order")
    list_filter = ("category", "is_active")
    search_fields = ("name", "description")
    list_editable = ("is_active", "display_order")


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ("title", "icon", "display_order")
    search_fields = ("title",)
    list_editable = ("display_order",)


@admin.register(ContactSettings)
class ContactSettingsAdmin(admin.ModelAdmin):
    list_display = ("heading", "email", "phone")


@admin.register(ContactEnquiry)
class ContactEnquiryAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "enquiry_type", "created_at")
    list_filter = ("enquiry_type", "created_at")
    search_fields = ("name", "email", "message")
    readonly_fields = (
        "name",
        "email",
        "phone",
        "company",
        "enquiry_type",
        "message",
        "created_at",
    )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(ConnectSection)
class ConnectSectionAdmin(admin.ModelAdmin):
    list_display = ("heading", "primary_button_text")


@admin.register(NavigationLink)
class NavigationLinkAdmin(admin.ModelAdmin):
    list_display = ("label", "url", "display_order", "is_active")
    list_editable = ("display_order", "is_active")


@admin.register(FooterSettings)
class FooterSettingsAdmin(admin.ModelAdmin):
    list_display = ("email", "phone")

# Register your models here.
