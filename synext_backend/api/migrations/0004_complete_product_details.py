from django.db import migrations


# 1. PRODUCT DETAILS
PRODUCTS = [
    {
        "name": "NEUROSYN-M™",
        "category": "Neurological Health",
        "description": (
            "Alpha Lipoic Acid 200 mg + Benfotiamine 100 mg + "
            "Folic Acid 1.5 mg + Inositol 100 mg + "
            "Methylcobalamin 1000 mcg + Vitamin B6 3 mg"
        ),
    },
]


# 2. FUNCTION TO IMPORT PRODUCTS
def populate_products(apps, schema_editor):
    Product = apps.get_model("api", "Product")
    ProductCategory = apps.get_model("api", "ProductCategory")
    db = schema_editor.connection.alias

    for item in PRODUCTS:
        category, _ = ProductCategory.objects.using(db).get_or_create(
            name=item["category"]
        )

        product, _ = Product.objects.using(db).get_or_create(
            name=item["name"]
        )

        fields_to_update = []

        if product.category_id is None:
            product.category = category
            fields_to_update.append("category")

        if not product.description:
            product.description = item["description"]
            fields_to_update.append("description")

        if fields_to_update:
            product.save(update_fields=fields_to_update)


# 3. DJANGO MIGRATION CLASS
class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_populate_website_content"),
    ]

    operations = [
        migrations.RunPython(
            populate_products,
            migrations.RunPython.noop,
        ),
    ]