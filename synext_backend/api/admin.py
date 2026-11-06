
from django.contrib import admin

from .models import (
    WebsiteSettings,
    HomeSection,
    AboutSection,
    AboutFeature,
    ProductCategory,
    Product,
    Feature,
    WhyChooseUsSection,
    WhyChooseUsItem,
    QualitySection,
    QualityItem,
    CommitmentSection,
    CommitmentItem,
    ConnectSection,
    NavigationLink,
    ContactSettings,
    ContactTopic,
    ContactEnquiry,
    FooterSettings,
    FooterLink,
)


# ==========================================
# ADMIN SITE SETTINGS
# ==========================================

admin.site.site_header = "Synexta Pharma Administration"
admin.site.site_title = "Synexta Pharma Admin"
admin.site.index_title = "Website Content Management"


# ==========================================
# 1. WEBSITE SETTINGS
# ==========================================

@admin.register(WebsiteSettings)
class WebsiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("site_name",)
    search_fields = ("site_name",)


# ==========================================
# 2. HOME / HERO SECTION
# ==========================================

@admin.register(HomeSection)
class HomeSectionAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "eyebrow",
        "button_text",
        "secondary_button_text",
    )
    search_fields = ("title", "subtitle")


# ==========================================
# 3. ABOUT SECTION
# ==========================================

@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "eyebrow")
    search_fields = ("title", "description")


@admin.register(AboutFeature)
class AboutFeatureAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "icon_key",
        "display_order",
    )
    search_fields = ("title", "description")
    list_editable = ("display_order",)
    ordering = ("display_order", "id")


# ==========================================
# 4. PRODUCT CATEGORIES
# ==========================================

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


# ==========================================
# 5. PRODUCTS
# ==========================================

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "is_active",
        "display_order",
    )

    list_filter = ("category", "is_active")

    search_fields = ("name", "description")

    list_editable = (
        "is_active",
        "display_order",
    )

    ordering = ("display_order", "id")

    fieldsets = (
        (
            "Basic Product Information",
            {
                "fields": (
                    "name",
                    "category",
                    "description",
                    "image",
                )
            },
        ),
        (
            "Product Details",
            {
                "fields": (
                    "prescription_label",
                    "form_and_pack",
                    "indication_segment",
                    "shelf_life",
                    "compliance",
                )
            },
        ),
        (
            "Therapeutic Information",
            {
                "fields": (
                    "indications",
                    "actives",
                ),
                "description": (
                    "Enter valid JSON. "
                    "Indications must be a list of strings; "
                    "actives must be a list of objects."
                ),
            },
        ),
        (
            "Website Display",
            {
                "fields": (
                    "is_active",
                    "display_order",
                )
            },
        ),
    )


# ==========================================
# 6. EXISTING FEATURES
# ==========================================

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "icon",
        "display_order",
    )
    search_fields = ("title", "description")
    list_editable = ("display_order",)
    ordering = ("display_order", "id")


# ==========================================
# 7. WHY CHOOSE US
# ==========================================

@admin.register(WhyChooseUsSection)
class WhyChooseUsSectionAdmin(admin.ModelAdmin):
    list_display = ("heading", "eyebrow")
    search_fields = ("heading", "description")


@admin.register(WhyChooseUsItem)
class WhyChooseUsItemAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "display_order",
    )
    search_fields = ("title", "description")
    list_editable = ("display_order",)
    ordering = ("display_order", "id")


# ==========================================
# 8. QUALITY ASSURANCE
# ==========================================

@admin.register(QualitySection)
class QualitySectionAdmin(admin.ModelAdmin):
    list_display = ("heading", "eyebrow")
    search_fields = ("heading",)


@admin.register(QualityItem)
class QualityItemAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "icon_key",
        "display_order",
    )
    search_fields = ("title", "description")
    list_editable = ("display_order",)
    ordering = ("display_order", "id")


# ==========================================
# 9. COMMITMENT
# ==========================================

@admin.register(CommitmentSection)
class CommitmentSectionAdmin(admin.ModelAdmin):
    list_display = ("heading", "eyebrow")
    search_fields = ("heading",)


@admin.register(CommitmentItem)
class CommitmentItemAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "icon_key",
        "display_order",
    )
    search_fields = ("title", "description")
    list_editable = ("display_order",)
    ordering = ("display_order", "id")


# ==========================================
# 10. CONNECT SECTION
# ==========================================

@admin.register(ConnectSection)
class ConnectSectionAdmin(admin.ModelAdmin):
    list_display = (
        "heading",
        "eyebrow",
        "primary_button_text",
        "secondary_button_text",
    )
    search_fields = ("heading", "description")


# ==========================================
# 11. NAVIGATION LINKS
# ==========================================

@admin.register(NavigationLink)
class NavigationLinkAdmin(admin.ModelAdmin):
    list_display = (
        "label",
        "url",
        "display_order",
        "is_active",
        "is_button",
    )

    search_fields = ("label", "url")

    list_filter = ("is_active", "is_button")

    list_editable = (
        "url",
        "display_order",
        "is_active",
        "is_button",
    )

    ordering = ("display_order", "id")


# ==========================================
# 12. CONTACT SETTINGS
# ==========================================

@admin.register(ContactSettings)
class ContactSettingsAdmin(admin.ModelAdmin):
    list_display = (
        "heading",
        "email",
        "phone",
    )
    search_fields = ("heading", "email")


@admin.register(ContactTopic)
class ContactTopicAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "icon_key",
        "display_order",
    )
    search_fields = ("title",)
    list_editable = ("display_order",)
    ordering = ("display_order", "id")


# ==========================================
# 13. CONTACT ENQUIRIES
# ==========================================

@admin.register(ContactEnquiry)
class ContactEnquiryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "enquiry_type",
        "created_at",
    )

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


# ==========================================
# 14. FOOTER SETTINGS
# ==========================================

@admin.register(FooterSettings)
class FooterSettingsAdmin(admin.ModelAdmin):
    list_display = ("email", "phone")


@admin.register(FooterLink)
class FooterLinkAdmin(admin.ModelAdmin):
    list_display = (
        "label",
        "url",
        "group",
        "display_order",
        "is_active",
    )

    list_filter = ("group", "is_active")

    search_fields = ("label", "url")

    list_editable = (
        "url",
        "display_order",
        "is_active",
    )

    ordering = ("group", "display_order", "id")
