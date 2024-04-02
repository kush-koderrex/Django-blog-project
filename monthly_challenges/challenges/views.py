from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect

from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
month_chal={
    "jan":"Jan is my birtyh day",
    "feb":"feb is Frbulious",
    "mar":"mar",
    "april":"april",
    "may":"may",
    "june":"june",
    "july":"july",
    "aug":"aug",
    "sep":"sep",
    "oct":"oct",
    "nov":"nov",
    "dec":None,
}

def index(request):
    list_itms = ""
    months = list(month_chal.keys())
    return render(request, "challenges/index.html",{
        "months" : months
    })
 
    # for month in months:
    #     cap_month = month.capitalize()
    #     month_path =reverse("month-challenge",args=[month])
    #     list_itms += f"<li><a href = '{month_path}'>{cap_month}</a></li>"

    # response_data = f"<ol>{list_itms}</ol>"
    # return HttpResponse(response_data)
    
    

def monthly_challenge_by_number(request,month):  
    months = list(month_chal.keys())
    if month > len(months):
        return HttpResponseNotFound("Endpoint Not Found")
        
    redirect_url = months[month-1]
    redirect_path = reverse("month-challenge",args=[redirect_url])
    return HttpResponseRedirect(redirect_path)
    



def monthly_challenge(request,month):
    try:
        chal_text = month_chal[month]
        cap_month = month.capitalize()
        return render(request,"challenges/challenge.html",{
            "text":chal_text,
            "month_name":cap_month,
        })
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("Endpoint Not Found ")