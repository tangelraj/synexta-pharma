from django.shortcuts import render
import json
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.views.decorators.csrf import csrf_exempt
import traceback
from .models import (
    HomeSection,
    AboutSection,
    Product,
    ContactSettings,
)
@csrf_exempt
def submit_enquiry(request):
    if request.method != "POST":
        return JsonResponse(
            {"error": "POST method required"},
            status=405
        )

    try:
        data = json.loads(request.body)

        name = data.get("name", "").strip()
        email = data.get("email", "").strip()
        phone = data.get("phone", "").strip()
        company = data.get("company", "").strip()
        enquiry_type = data.get("enquiryType", "").strip()
        message = data.get("message", "").strip()

        if not all([name, email, enquiry_type, message]):
            return JsonResponse(
                {"error": "Please fill all required fields"},
                status=400
            )

        email_body = f"""
New Enquiry - Synexta Pharma

Name: {name}
Email: {email}
Phone: {phone}
Company: {company}
Enquiry Type: {enquiry_type}

Message:
{message}
"""

        enquiry_email = EmailMessage(
            subject=f"New Website Enquiry - {name}",
            body=email_body,
            to=["tangelraj@gmail.com"],
            reply_to=[email],
        )

        enquiry_email.send(fail_silently=False)

        return JsonResponse({
            "success": True,
            "message": "Enquiry submitted successfully!"
        })

    except (json.JSONDecodeError, AttributeError):
        return JsonResponse(
            {"error": "Invalid enquiry data"},
            status=400
        )
    except Exception:
        traceback.print_exc()

        return JsonResponse(
            {"error": "Unable to send enquiry right now"},
            status=500
        )
def home_data(request):
    home = HomeSection.objects.first()

    if not home:
        return JsonResponse({"message": "No home content found"})

    return JsonResponse({
        "title": home.title,
        "subtitle": home.subtitle,
        "banner_image": image_url(request, home.banner_image),
        "button_text": home.button_text,
        "button_link": home.button_link,
    })


def about_data(request):
    about = AboutSection.objects.first()

    if not about:
        return JsonResponse({"message": "No about content found"})

    return JsonResponse({
        "title": about.title,
        "description": about.description,
        "image": image_url(request, about.image),
    })


def products_data(request):
    products = Product.objects.filter(
        is_active=True
    ).select_related("category").order_by("display_order", "id")

    data = []

    for product in products:
        data.append({
            "id": product.id,
            "name": product.name,
            "category": product.category.name if product.category else "",
            "description": product.description,
            "image": image_url(request, product.image),
        })

    return JsonResponse(data, safe=False)


def contact_data(request):
    contact = ContactSettings.objects.first()

    if not contact:
        return JsonResponse({"message": "No contact settings found"})

    return JsonResponse({
        "heading": contact.heading,
        "description": contact.description,
        "email": contact.email,
        "phone": contact.phone,
        "address": contact.address,
    })
# Create your views here.
