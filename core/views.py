from bs4 import BeautifulSoup
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator
import json
from .models import *

# Create your views here.
def home(request):
    navbar_items    = NavbarItem.objects.filter(is_active=True, parent=None)
    services        = Service.objects.all().order_by("order_number")
    sliders         = Slider.objects.all()
    section_title   = SectionTitle.objects.first()
    partners        = Partner.objects.all()
    about_content   = AboutUs.objects.all().first()
    monthly_plans   = PricingPlan.objects.filter(plan_type="monthly")
    yearly_plans    = PricingPlan.objects.filter(plan_type="yearly")
    support_info    = SupportInfo.objects.first()
    footer          = Footer.objects.first()
    context = {
        "navbar_items"  : navbar_items,
        "sliders"       : sliders,
        "services"      : services,
        "section_title" : section_title,
        "partners"      : partners,
        "about_content" : about_content,
        "monthly_plans" : monthly_plans,
        "yearly_plans"  : yearly_plans,
        "support_info"  : support_info,
        "footer"        : footer,
    }
    print(about_content)
    return render(request, 'index.html', context)

def get_mobile_details(request):
    if request.method == "POST":
        # Get the query from the POST request
        query = request.POST.get("query")
        if not query:
            return JsonResponse({"error": "No query provided"}, status=400)
        
        # Define the URL and headers
        url = "https://www.simdata.store/"
        headers = {
            "Cookie": "PHPSESSID=b2f50bc4ecc59c46046d2a812419c935; _gcl_au=1.1.1366805211.1734018718; yneEinx=1",
            "Cache-Control": "max-age=0",
            "Sec-Ch-Ua": '"Chromium";v="129", "Not=A?Brand";v="8"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Linux"',
            "Accept-Language": "en-US,en;q=0.9",
            "Origin": "https://www.simdata.store",
            "Content-Type": "application/x-www-form-urlencoded",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.71 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://www.simdata.store/",
            "Accept-Encoding": "gzip, deflate, br",
            "Priority": "u=0, i"
        }

        # Define the POST data
        data = {"query": query}

        try:
            # Send POST request
            response = requests.post(url, headers=headers, data=data)
            response.raise_for_status()  # Raise error for bad HTTP status

            # Parse the response content
            soup = BeautifulSoup(response.text, "html.parser")
            table = soup.find("table")
            
            if not table:
                return JsonResponse({"error": "No table found in response"}, status=404)

            # Extract table rows
            rows = table.find("tbody").find_all("tr")
            table_data = []

            for row in rows:
                row_data = {}
                for cell in row.find_all("td"):
                    key = cell.get("data-label", "Unknown").strip()
                    value = cell.text.strip()
                    row_data[key] = value
                table_data.append(row_data)

            # Return table data as JSON
            return JsonResponse({"data": table_data}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return render(request, home)

def save_phone_detail(request):
    if request.method == 'POST':
        # Get the phone details from the request
        try:
            data = json.loads(request.POST.get('phoneDetail'))  # The data sent from the frontend
            
            # Create a new PhoneDetail object and save it to the database
            phone_detail = PhoneDetail(
                number=data['number'],
                name=data['name'],
                father_name=data['father_name'],
                cnic=data['cnic'],
                address=data['address']
            )
            phone_detail.save()

            # Return success response
            return JsonResponse({'status': 'danger', 'message': 'Phone detail saved successfully.'})
        
        except json.JSONDecodeError:
            return JsonResponse({'status': 'danger', 'message': 'Invalid data format.'})
        
        except Exception as e:
            return JsonResponse({'status': 'danger', 'message': str(e)})

    return JsonResponse({'status': 'danger', 'message': 'Invalid request method.'})