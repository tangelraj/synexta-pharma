
import json
import logging
from urllib import request as urlrequest
from urllib import error as urlerror

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import (
    HomeSection,
    AboutSection,
    Product,
    ContactSettings,
)


logger = logging.getLogger(__name__)


# --------------------------------------------------
# IMAGE URL HELPER
# --------------------------------------------------

def image_url(request, image):
    if not image:
        return None

    return request.build_absolute_uri(image.url)


# --------------------------------------------------
# CONTACT ENQUIRY
# --------------------------------------------------

@csrf_exempt
def submit_enquiry(request):
    if request.method != "POST":
        return JsonResponse(
            {"error": "POST method required"},
            status=405
        )

    if len(request.body) > 20000:
        return JsonResponse(
            {"error": "Enquiry is too large"},
            status=413
        )

    try:
        data = json.loads(request.body)

        if not isinstance(data, dict):
            raise ValueError("Invalid JSON object")

        name = str(data.get("name") or "").strip()
        email = str(data.get("email") or "").strip()
        phone = str(data.get("phone") or "").strip()
        company = str(data.get("company") or "").strip()
        enquiry_type = str(data.get("enquiryType") or "").strip()
        message = str(data.get("message") or "").strip()

        if not all([name, email, enquiry_type, message]):
            return JsonResponse(
                {"error": "Please fill all required fields"},
                status=400
            )

        validate_email(email)

        if (
            len(name) > 150
            or len(email) > 254
            or len(phone) > 30
            or len(company) > 150
            or len(enquiry_type) > 100
            or len(message) > 5000
        ):
            return JsonResponse(
                {"error": "One or more fields are too long"},
                status=400
            )

    except (ValueError, TypeError, ValidationError):
        return JsonResponse(
            {"error": "Invalid enquiry data or email address"},
            status=400
        )

    api_key = getattr(settings, "RESEND_API_KEY", "")
    sender = getattr(settings, "RESEND_FROM_EMAIL", "")
    recipient = getattr(settings, "ENQUIRY_TO_EMAIL", "")

    if not all([api_key, sender, recipient]):
        logger.error("Resend email configuration is missing")
        return JsonResponse(
            {"error": "Email service is not configured"},
            status=503
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

    payload = {
        "from": sender,
        "to": [recipient],
        "subject": "New Website Enquiry - Synexta Pharma",
        "text": email_body,
        "reply_to": email,
    }

    http_request = urlrequest.Request(
        "https://api.resend.com/emails",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "User-Agent": "SynextaPharma/1.0",
        },
        method="POST",
    )

    try:
        with urlrequest.urlopen(http_request, timeout=15) as response:
            result = json.loads(response.read().decode("utf-8"))

        if not result.get("id"):
            logger.error("Resend response did not include an email ID")
            return JsonResponse(
                {"error": "Unable to send enquiry right now"},
                status=502
            )

        return JsonResponse({
            "success": True,
            "message": "Enquiry submitted successfully!"
        })

    except urlerror.HTTPError as exc:
        logger.error("Resend API returned HTTP %s", exc.code)
        return JsonResponse(
            {"error": "Unable to send enquiry right now"},
            status=502
        )

    except (urlerror.URLError, TimeoutError, ValueError, OSError):
        logger.exception("Resend email request failed")
        return JsonResponse(
            {"error": "Unable to send enquiry right now"},
            status=502
        )


# --------------------------------------------------
# HOME API
# --------------------------------------------------

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


# --------------------------------------------------
# ABOUT API
# --------------------------------------------------

def about_data(request):
    about = AboutSection.objects.first()

    if not about:
        return JsonResponse({"message": "No about content found"})

    return JsonResponse({
        "title": about.title,
        "description": about.description,
        "image": image_url(request, about.image),
    })


# --------------------------------------------------
# PRODUCTS API
# --------------------------------------------------

def products_data(request):
    products = Product.objects.filter(
        is_active=True
    ).select_related("category").order_by("display_order", "id")

    data = []

    for product in products:
        data.append({
            "id": product.id,
            "name": product.name,
            "category": (
                product.category.name
                if product.category
                else ""
            ),
            "description": product.description,
            "image": image_url(request, product.image),
        })

    return JsonResponse(data, safe=False)


# --------------------------------------------------
# CONTACT DETAILS API
# --------------------------------------------------

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
