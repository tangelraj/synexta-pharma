from django.shortcuts import render
import json
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.views.decorators.csrf import csrf_exempt
import traceback

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
# Create your views here.
