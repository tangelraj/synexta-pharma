
from django.db import migrations


def populate_website_content(apps, schema_editor):

    db = schema_editor.connection.alias

    WebsiteSettings = apps.get_model("api", "WebsiteSettings")
    HomeSection = apps.get_model("api", "HomeSection")
    AboutSection = apps.get_model("api", "AboutSection")
    AboutFeature = apps.get_model("api", "AboutFeature")
    Product = apps.get_model("api", "Product")
    WhyChooseUsSection = apps.get_model("api", "WhyChooseUsSection")
    WhyChooseUsItem = apps.get_model("api", "WhyChooseUsItem")
    QualitySection = apps.get_model("api", "QualitySection")
    QualityItem = apps.get_model("api", "QualityItem")
    CommitmentSection = apps.get_model("api", "CommitmentSection")
    CommitmentItem = apps.get_model("api", "CommitmentItem")
    ConnectSection = apps.get_model("api", "ConnectSection")
    NavigationLink = apps.get_model("api", "NavigationLink")
    ContactSettings = apps.get_model("api", "ContactSettings")
    ContactTopic = apps.get_model("api", "ContactTopic")
    FooterSettings = apps.get_model("api", "FooterSettings")
    FooterLink = apps.get_model("api", "FooterLink")

    # ==========================================
    # WEBSITE SETTINGS
    # ==========================================

    if not WebsiteSettings.objects.using(db).exists():
        WebsiteSettings.objects.using(db).create(
            site_name="Synexta Pharma"
        )

    # ==========================================
    # HOME SECTION
    # ==========================================

    if not HomeSection.objects.using(db).exists():
        HomeSection.objects.using(db).create(
            title="Synexta Pharma",
            eyebrow="Trusted Pharmaceutical Solutions",
            subtitle="",
            button_text="Explore Products",
            button_link="/#products",
            secondary_button_text="Contact Our Team",
            secondary_button_link="/#contact",
        )

    # ==========================================
    # ABOUT SECTION
    # ==========================================

    if not AboutSection.objects.using(db).exists():
        AboutSection.objects.using(db).create(
            title="About Synexta Pharma",
            eyebrow="About Us",
            description="",
        )

    about_features = [
        (
            "Quality-Focused Approach",
            "Every formulation is presented with care, "
            "clarity and consistency.",
        ),
        (
            "Reliable Pharmaceutical Solutions",
            "A focused portfolio built around everyday "
            "healthcare needs.",
        ),
        (
            "Healthcare-Centered Commitment",
            "We work alongside healthcare professionals "
            "for better patient care.",
        ),
    ]

    for order, (title, description) in enumerate(
        about_features, 1
    ):
        AboutFeature.objects.using(db).get_or_create(
            title=title,
            defaults={
                "description": description,
                "display_order": order,
            },
        )

    # ==========================================
    # WHY CHOOSE US SECTION
    # ==========================================

    if not WhyChooseUsSection.objects.using(db).exists():
        WhyChooseUsSection.objects.using(db).create(
            eyebrow="Why Choose Us",
            heading="Why Choose Synexta Pharma?",
            description=(
                "We keep things simple: dependable products, "
                "clear information and a people-first approach."
            ),
        )

    reasons = [
        (
            "Quality first",
            "Formulations selected and presented "
            "with a focus on quality.",
        ),
        (
            "Product clarity",
            "Exact names, strengths and compositions "
            "— nothing hidden.",
        ),
        (
            "Responsible communication",
            "Accurate information without exaggerated claims.",
        ),
        (
            "Professional engagement",
            "A team that listens to healthcare "
            "professionals and partners.",
        ),
    ]

    for order, (title, description) in enumerate(
        reasons, 1
    ):
        WhyChooseUsItem.objects.using(db).get_or_create(
            title=title,
            defaults={
                "description": description,
                "display_order": order,
            },
        )

    # ==========================================
    # QUALITY ASSURANCE SECTION
    # ==========================================

    if not QualitySection.objects.using(db).exists():
        QualitySection.objects.using(db).create(
            eyebrow="Quality Assurance",
            heading="Quality at the Heart of Every Formulation",
        )

    quality_items = [
        (
            "Commitment to Quality",
            "Quality guides every product we bring to market.",
        ),
        (
            "Product Information Transparency",
            "Clear, accurate compositions for every formulation.",
        ),
        (
            "Consistent Brand Standards",
            "A uniform standard of presentation across our range.",
        ),
        (
            "Healthcare Professional Support",
            "Responsive help for professionals and partners.",
        ),
    ]

    for order, (title, description) in enumerate(
        quality_items, 1
    ):
        QualityItem.objects.using(db).get_or_create(
            title=title,
            defaults={
                "description": description,
                "display_order": order,
            },
        )

    # ==========================================
    # COMMITMENT SECTION
    # ==========================================

    if not CommitmentSection.objects.using(db).exists():
        CommitmentSection.objects.using(db).create(
            eyebrow="Our Commitment",
            heading="Quality at the Heart of Every Formulation",
        )

    for order, (title, description) in enumerate(
        quality_items, 1
    ):
        CommitmentItem.objects.using(db).get_or_create(
            title=title,
            defaults={
                "description": description,
                "display_order": order,
            },
        )

    # ==========================================
    # CONNECT SECTION
    # ==========================================

    if not ConnectSection.objects.using(db).exists():
        ConnectSection.objects.using(db).create(
            eyebrow="Let's Connect",
            heading="Let's Connect for Better Healthcare Solutions",
            description=(
                "Connect with our team to learn more about "
                "our pharmaceutical product portfolio "
                "and business enquiries."
            ),
            primary_button_text="Contact Us",
            primary_button_link="/contact",
            secondary_button_text="Explore Products",
            secondary_button_link="/products",
        )

    # ==========================================
    # CONTACT SETTINGS
    # ==========================================

    if not ContactSettings.objects.using(db).exists():
        ContactSettings.objects.using(db).create(
            eyebrow="Contact Us",
            heading="Get in Touch",
            description=(
                "Have a question about our products or a "
                "business enquiry? Send us a message and "
                "our team will get back to you."
            ),
        )

    contact_topics = [
        "Product information requests",
        "Distribution & business partnerships",
        "Healthcare professional support",
    ]

    for order, title in enumerate(contact_topics, 1):
        ContactTopic.objects.using(db).get_or_create(
            title=title,
            defaults={
                "display_order": order,
            },
        )

    # ==========================================
    # NAVIGATION LINKS
    # ==========================================

    navigation = [
        ("Home", "/#home"),
        ("About Us", "/#about"),
        ("Products", "/#products"),
        ("Why Choose Us", "/#why-choose-us"),
        ("Quality Assurance", "/#quality"),
        ("Contact", "/#contact"),
        ("Explore Products", "/#products"),
    ]

    for order, (label, url) in enumerate(navigation, 1):
        NavigationLink.objects.using(db).get_or_create(
            label=label,
            defaults={
                "url": url,
                "display_order": order,
                "is_active": True,
                "is_button": label == "Explore Products",
            },
        )

    # ==========================================
    # FOOTER SETTINGS
    # ==========================================

    if not FooterSettings.objects.using(db).exists():
        FooterSettings.objects.using(db).create(
            description="Quality Medicines. Trusted Care.",
            copyright_text=(
                "© 2026 Synexta Pharma. All rights reserved."
            ),
        )

    # ==========================================
    # FOOTER LINKS
    # ==========================================

    quick_links = [
        ("Home", "#home"),
        ("About Us", "#about"),
        ("Products", "#products"),
        ("Our Expertise", "#why-choose-us"),
        ("Quality Assurance", "#quality"),
        ("Contact", "#contact"),
    ]

    product_links = [
        ("NEUROSYN-M™", "/products"),
        ("TRYPSYN-R™", "/products"),
        ("BETASYN™ 8/16", "/products"),
        ("PREGASYN™", "/products"),
        ("PANTOSYN™ 20/40", "/products"),
        ("CEFIXA™ 200", "/products"),
        ("PREGASYN™ FORTE", "/products"),
    ]

    legal_links = [
        ("Privacy Policy", "/privacy-policy"),
        ("Terms and Conditions", "/terms-and-conditions"),
    ]

    for group, links in [
        ("quick", quick_links),
        ("product", product_links),
        ("legal", legal_links),
    ]:
        for order, (label, url) in enumerate(links, 1):
            FooterLink.objects.using(db).get_or_create(
                group=group,
                label=label,
                defaults={
                    "url": url,
                    "display_order": order,
                    "is_active": True,
                },
            )

    # ==========================================
    # SEVEN EXISTING PRODUCTS
    # ==========================================

    product_names = [
        "NEUROSYN-M™",
        "PANTOSYN™ 20/40",
        "TRYPSYN-R™",
        "CEFIXA™ 200",
        "BETASYN™ 8/16",
        "PREGASYN™ FORTE",
        "PREGASYN™",
    ]

    for order, name in enumerate(product_names, 1):
        Product.objects.using(db).get_or_create(
            name=name,
            defaults={
                "description": "",
                "display_order": order,
                "is_active": True,
            },
        )


class Migration(migrations.Migration):

    dependencies = [
        (
            "api",
            "0002_aboutfeature_commitmentitem_commitmentsection_and_more",
        ),
    ]

    operations = [
        migrations.RunPython(
            populate_website_content,
            migrations.RunPython.noop,
        ),
    ]
