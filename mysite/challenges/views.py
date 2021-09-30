from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "1. Zero Eating Out",
    "february": "2. Track Your Spending",
    "march": "3. Try a No-Spend Month",
    "april": "4. No Retail Shopping",
    "may": "5. Pay In Cash Only",
    "june": "6. Avoid Social Media While Working",
    "july": "7. Meal Prep Your Lunch",
    "august": "8. Make One New Connection a Week",
    "september": "9. Work Breaks into Your Daily Routine",
    "october": "10. Read a Chapter of a Book a Day",
    "november": "11. Start a Blog (and Post Once a Week)",
    "december": "12. Clean Up After You’re Done"
}


def index(request):
    list_items = ""

    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    
    response_data = f"<ul>{list_items}</ul>"


    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("invalid month")


    redirect_month = months[month -1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("This month is not supported.")
        
    