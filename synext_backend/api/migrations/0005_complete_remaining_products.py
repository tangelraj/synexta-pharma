
from django.db import migrations


PRODUCTS = [
    {
        "name": "PANTOSYN™ 20/40",
        "category": "Gastrointestinal Health",
        "description": "Pantoprazole 20 mg / 40 mg Tablets",
    },
    {
        "name": "TRYPSYN-R™",
        "category": "Musculoskeletal Support",
        "description": (
            "Bromelain 90 mg + Rutoside Trihydrate 100 mg "
            "+ Trypsin 48 mg"
        ),
    },
    {
        "name": "CEFIXA™ 200",
        "category": "Other Formulations",
        "description": "Cefixime 200 mg Tablets",
    },
    {
        "name": "BETASYN™ 8/16",
        "category": "Other Formulations",
        "description": "Betahistine 8 mg / 16 mg Tablets",
    },
    {
        "name": "PREGASYN™ FORTE",
        "category": "Neurological Health",
        "description": (
            "Pregabalin 75 mg + Methylcobalamin 1500 mcg"
        ),
    },
    {
        "name": "PREGASYN™",
        "category": "Neurological Health",
        "description": (
            "Methylcobalamin 750 mcg + Pregabalin 50 mg"
        ),
    },
]


def populate_remaining_products(apps, schema_editor):
    Product = apps.get_model("api", "Product")
    ProductCategory = apps.get_model("api", "ProductCategory")

    db = schema_editor.connection.alias

    for item in PRODUCTS:
        category, _ = ProductCategory.objects.using(db).get_or_create(
            name=item["category"]
        )

        product, _ = Product.objects.using(db).get_or_create(
            name=item["name"],
            defaults={
                "is_active": True,
            },
        )

        update_fields = []

        if product.category_id is None:
            product.category = category
            update_fields.append("category")

        if not product.description:
            product.description = item["description"]
            update_fields.append("description")

        if update_fields:
            product.save(update_fields=update_fields)


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_complete_product_details"),
    ]

    operations = [
        migrations.RunPython(
            populate_remaining_products,
            migrations.RunPython.noop,
        ),
    ]
