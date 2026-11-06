
from django.db import migrations


ABOUT_TITLE = "Committed to Quality. Focused on Care."

ABOUT_DESCRIPTION = (
    "Synexta Pharma offers a range of pharmaceutical "
    "formulations designed to support diverse healthcare needs. "
    "Our approach is built on quality, transparency and a "
    "genuine commitment to trusted healthcare solutions."
)

FEATURES = [
    (
        "Quality-Focused Approach",
        "Every formulation is presented with care, clarity "
        "and consistency.",
        "award",
    ),
    (
        "Reliable Pharmaceutical Solutions",
        "A focused portfolio built around everyday healthcare needs.",
        "flask-conical",
    ),
    (
        "Healthcare-Centered Commitment",
        "We work alongside healthcare professionals "
        "for better patient care.",
        "heart-pulse",
    ),
]


def populate_about(apps, schema_editor):
    AboutSection = apps.get_model("api", "AboutSection")
    AboutFeature = apps.get_model("api", "AboutFeature")
    db = schema_editor.connection.alias

    about = AboutSection.objects.using(db).first()

    if about is None:
        AboutSection.objects.using(db).create(
            title=ABOUT_TITLE,
            eyebrow="About Synexta Pharma",
            description=ABOUT_DESCRIPTION,
        )
    else:
        updates = []

        if about.title in ("", "About Synexta Pharma"):
            about.title = ABOUT_TITLE
            updates.append("title")

        if not about.description:
            about.description = ABOUT_DESCRIPTION
            updates.append("description")

        if about.eyebrow in ("", "About Us"):
            about.eyebrow = "About Synexta Pharma"
            updates.append("eyebrow")

        if updates:
            about.save(update_fields=updates)

    for order, (title, description, icon_key) in enumerate(
        FEATURES, start=1
    ):
        feature, created = AboutFeature.objects.using(db).get_or_create(
            title=title,
            defaults={
                "description": description,
                "icon_key": icon_key,
                "display_order": order,
            },
        )

        if not created:
            updates = []

            if not feature.description:
                feature.description = description
                updates.append("description")

            if not feature.icon_key:
                feature.icon_key = icon_key
                updates.append("icon_key")

            if updates:
                feature.save(update_fields=updates)


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_complete_remaining_products"),
    ]

    operations = [
        migrations.RunPython(
            populate_about,
            migrations.RunPython.noop,
        ),
    ]
