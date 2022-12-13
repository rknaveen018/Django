from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def month_view(request, months):
    month_name = {"january":"Hey there your in January",
                "february":"Hey there your in February",
                "march":"Hey there your in March",
                "april":"Hey there your in April",
                "may":"Hey there your in May",
                "june":"Hey there your in June",
                "july":"Hey there your in July",
                "august":"Hey there your in August",
                "september":"Hey there your in September",
                "october":"Hey there your in October",
                "november":"Hey there your in November",
                "december":"Hey there your in December"
}

    if months in month_name:
        return HttpResponse(month_name[months])
    else:
        return HttpResponseNotFound("Try with different text")