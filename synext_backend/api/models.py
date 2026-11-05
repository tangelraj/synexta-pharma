from django.db import models

from django.db import models


class WebsiteSettings(models.Model):
    site_name = models.CharField(max_length=200, default="Synexta Pharma")
    logo = models.ImageField(upload_to="website/", blank=True, null=True)
    favicon = models.ImageField(upload_to="website/", blank=True, null=True)

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name_plural = "Website Settings"


class HomeSection(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.TextField(blank=True)
    banner_image = models.ImageField(upload_to="home/", blank=True, null=True)
    button_text = models.CharField(max_length=100, blank=True)
    button_link = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.title


class AboutSection(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to="about/", blank=True, null=True)

    def __str__(self):
        return self.title


class ProductCategory(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Feature(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Icon name, for example: shield-check"
    )
    image = models.ImageField(upload_to="features/", blank=True, null=True)
    display_order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class ContactSettings(models.Model):
    heading = models.CharField(max_length=200, default="Get in Touch")
    description = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name_plural = "Contact Settings"


class ContactEnquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    company = models.CharField(max_length=200, blank=True)
    enquiry_type = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        verbose_name_plural = "Contact Enquiries"


class ConnectSection(models.Model):
    heading = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    background_image = models.ImageField(
        upload_to="connect/",
        blank=True,
        null=True
    )
    primary_button_text = models.CharField(max_length=100, blank=True)
    primary_button_link = models.CharField(max_length=250, blank=True)
    secondary_button_text = models.CharField(max_length=100, blank=True)
    secondary_button_link = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.heading


class NavigationLink(models.Model):
    label = models.CharField(max_length=100)
    url = models.CharField(max_length=250)
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.label


class FooterSettings(models.Model):
    description = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    address = models.TextField(blank=True)
    copyright_text = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return "Footer Settings"

    class Meta:
        verbose_name_plural = "Footer Settings"

# Create your models here.
