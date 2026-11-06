
from django.db import models


# ==========================================
# 1. WEBSITE SETTINGS
# ==========================================

class WebsiteSettings(models.Model):
    site_name = models.CharField(
        max_length=200,
        default="Synexta Pharma"
    )
    logo = models.ImageField(
        upload_to="website/",
        blank=True,
        null=True
    )
    favicon = models.ImageField(
        upload_to="website/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name_plural = "Website Settings"


# ==========================================
# 2. HOME / HERO SECTION
# ==========================================

class HomeSection(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.TextField(blank=True)

    banner_image = models.ImageField(
        upload_to="home/",
        blank=True,
        null=True
    )

    button_text = models.CharField(
        max_length=100,
        blank=True
    )
    button_link = models.CharField(
        max_length=250,
        blank=True
    )

    eyebrow = models.CharField(
        max_length=150,
        blank=True
    )
    secondary_button_text = models.CharField(
        max_length=100,
        blank=True
    )
    secondary_button_link = models.CharField(
        max_length=250,
        blank=True
    )

    def __str__(self):
        return self.title


# ==========================================
# 3. ABOUT SECTION
# ==========================================

class AboutSection(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()

    image = models.ImageField(
        upload_to="about/",
        blank=True,
        null=True
    )

    eyebrow = models.CharField(
        max_length=150,
        blank=True
    )

    def __str__(self):
        return self.title


# ==========================================
# 4. ABOUT FEATURES
# ==========================================

class AboutFeature(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    icon_key = models.CharField(
        max_length=50,
        blank=True
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ["display_order", "id"]

    def __str__(self):
        return self.title


# ==========================================
# 5. PRODUCT CATEGORY
# ==========================================

class ProductCategory(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


# ==========================================
# 6. PRODUCTS
# ==========================================

class Product(models.Model):
    name = models.CharField(max_length=200)

    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    description = models.TextField(blank=True)

    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True)

    display_order = models.PositiveIntegerField(
        default=0
    )

    prescription_label = models.CharField(
        max_length=150,
        blank=True
    )

    form_and_pack = models.CharField(
        max_length=200,
        blank=True
    )

    indication_segment = models.CharField(
        max_length=200,
        blank=True
    )

    shelf_life = models.CharField(
        max_length=200,
        blank=True
    )

    compliance = models.CharField(
        max_length=200,
        blank=True
    )

    indications = models.JSONField(
        default=list,
        blank=True
    )

    actives = models.JSONField(
        default=list,
        blank=True
    )

    def __str__(self):
        return self.name


# ==========================================
# 7. EXISTING FEATURES
# ==========================================

class Feature(models.Model):
    title = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Icon name, for example: shield-check"
    )

    image = models.ImageField(
        upload_to="features/",
        blank=True,
        null=True
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    def __str__(self):
        return self.title


# ==========================================
# 8. WHY CHOOSE US SECTION
# ==========================================

class WhyChooseUsSection(models.Model):
    eyebrow = models.CharField(
        max_length=150,
        blank=True
    )

    heading = models.CharField(max_length=250)

    description = models.TextField(blank=True)

    image = models.ImageField(
        upload_to="why_choose_us/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.heading


# ==========================================
# 9. WHY CHOOSE US ITEMS
# ==========================================

class WhyChooseUsItem(models.Model):
    title = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    display_order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ["display_order", "id"]

    def __str__(self):
        return self.title


# ==========================================
# 10. QUALITY ASSURANCE SECTION
# ==========================================

class QualitySection(models.Model):
    eyebrow = models.CharField(
        max_length=150,
        blank=True
    )

    heading = models.CharField(max_length=250)

    background_image = models.ImageField(
        upload_to="quality/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.heading


# ==========================================
# 11. QUALITY ASSURANCE ITEMS
# ==========================================

class QualityItem(models.Model):
    title = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    icon_key = models.CharField(
        max_length=50,
        blank=True
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ["display_order", "id"]

    def __str__(self):
        return self.title


# ==========================================
# 12. COMMITMENT SECTION
# ==========================================

class CommitmentSection(models.Model):
    eyebrow = models.CharField(
        max_length=150,
        blank=True
    )

    heading = models.CharField(max_length=250)

    background_image = models.ImageField(
        upload_to="commitment/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.heading


# ==========================================
# 13. COMMITMENT ITEMS
# ==========================================

class CommitmentItem(models.Model):
    title = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    icon_key = models.CharField(
        max_length=50,
        blank=True
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ["display_order", "id"]

    def __str__(self):
        return self.title


# ==========================================
# 14. CONNECT SECTION
# ==========================================

class ConnectSection(models.Model):
    heading = models.CharField(max_length=250)

    description = models.TextField(blank=True)

    background_image = models.ImageField(
        upload_to="connect/",
        blank=True,
        null=True
    )

    primary_button_text = models.CharField(
        max_length=100,
        blank=True
    )

    primary_button_link = models.CharField(
        max_length=250,
        blank=True
    )

    secondary_button_text = models.CharField(
        max_length=100,
        blank=True
    )

    secondary_button_link = models.CharField(
        max_length=250,
        blank=True
    )

    eyebrow = models.CharField(
        max_length=150,
        blank=True
    )

    def __str__(self):
        return self.heading


# ==========================================
# 15. NAVIGATION LINKS
# ==========================================

class NavigationLink(models.Model):
    label = models.CharField(max_length=100)

    url = models.CharField(max_length=250)

    display_order = models.PositiveIntegerField(
        default=0
    )

    is_active = models.BooleanField(default=True)

    is_button = models.BooleanField(default=False)

    class Meta:
        ordering = ["display_order", "id"]

    def __str__(self):
        return self.label


# ==========================================
# 16. CONTACT SETTINGS
# ==========================================

class ContactSettings(models.Model):
    heading = models.CharField(
        max_length=200,
        default="Get in Touch"
    )

    description = models.TextField(blank=True)

    email = models.EmailField(blank=True)

    phone = models.CharField(
        max_length=30,
        blank=True
    )

    address = models.TextField(blank=True)

    eyebrow = models.CharField(
        max_length=150,
        blank=True
    )

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name_plural = "Contact Settings"


# ==========================================
# 17. CONTACT TOPICS
# ==========================================

class ContactTopic(models.Model):
    title = models.CharField(max_length=200)

    icon_key = models.CharField(
        max_length=50,
        blank=True
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ["display_order", "id"]

    def __str__(self):
        return self.title


# ==========================================
# 18. CONTACT ENQUIRIES
# ==========================================

class ContactEnquiry(models.Model):
    name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(
        max_length=30,
        blank=True
    )

    company = models.CharField(
        max_length=200,
        blank=True
    )

    enquiry_type = models.CharField(max_length=100)

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        verbose_name_plural = "Contact Enquiries"


# ==========================================
# 19. FOOTER SETTINGS
# ==========================================

class FooterSettings(models.Model):
    description = models.TextField(blank=True)

    email = models.EmailField(blank=True)

    phone = models.CharField(
        max_length=30,
        blank=True
    )

    address = models.TextField(blank=True)

    copyright_text = models.CharField(
        max_length=250,
        blank=True
    )

    def __str__(self):
        return "Footer Settings"

    class Meta:
        verbose_name_plural = "Footer Settings"


# ==========================================
# 20. FOOTER LINKS
# ==========================================

class FooterLink(models.Model):
    LINK_GROUPS = [
        ("quick", "Quick Links"),
        ("product", "Product Links"),
        ("legal", "Legal Links"),
    ]

    label = models.CharField(max_length=150)

    url = models.CharField(max_length=250)

    group = models.CharField(
        max_length=20,
        choices=LINK_GROUPS,
        default="quick"
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["group", "display_order", "id"]

    def __str__(self):
        return self.label
