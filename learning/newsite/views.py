from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
actions = {'1':'Addition', '2':'Subtraction', '3':'Division', '4':'Multiple'}

def home(request):
    return render(request, "home.html", {'actions': actions.values})

def action(request, val):
    return render(request, "action.html", {'action': val.title()})

def result(request,val):

    try:
        # Get numbers from the request, with default values if not provided
        num1 = int(request.GET.get('num1', 0))
        num2 = int(request.GET.get('num2', 0))
    
        # Perform the requested operation
        if val == "Addition":
            res = num1 + num2
        elif val == "Subtraction":
            res = num1 - num2
        elif val == "Multiple":
            res = num1 * num2
        elif val == "Division":
            if num2 == 0:
                return HttpResponse("Error: Division by zero is not allowed.")
            res = num1 / num2
        else:
            pass
    
        return render(request, "result.html", {'result': res})
    
    except:
        return HttpResponse("Invalid input/Empty input. Please provide valid numbers.")
    