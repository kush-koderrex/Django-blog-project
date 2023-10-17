from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect

from django.urls import reverse

# Create your views here.
month_chal={
    "jan":"Jan",
    "feb":"feb",
    "mar":"mar",
    "april":"april",
    "may":"may",
    "june":"june",
    "july":"july",
    "aug":"aug",
    "sep":"sep",
    "oct":"oct",
    "nov":"nov",
    "dec":"dec",
}

def index(request,month):
    return HttpResponse()
    
    

def monthly_challenge_by_number(request,month):  
    months = list(month_chal.keys())
    if month > len(months):
        return HttpResponseNotFound("Endpoint Not Found ")
        
    redirect_url = months[month-1]
    redirect_path = reverse("month-challenge",args=[redirect_url])
    return HttpResponseRedirect(redirect_path)
    



def monthly_challenge(request,month):
    try:
        chal_text = month_chal[month]
        response_data = f"<h1>{chal_text}<h1/>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("Endpoint Not Found ")