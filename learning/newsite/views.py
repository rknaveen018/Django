from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
actions = {'1':'add', '2':'sub', '3':'div', '4':'mul'}

def home(request):
    return render(request, "home.html", {'actions': actions.values})

def action(request, val):
    return render(request, "action.html", {'action': val})

def result(request,val):

    try:
        num1 = int(request.GET.get('num1'))
        num2 = int(request.GET.get('num2'))
    
        if val == "add":
            res = num1 + num2
        elif val == "sub":
            res = num1 - num2
        elif val == "mul":
            res = num1 * num2
        elif val == "div":
            res = num1 / num2 
        else:
            pass

        return render(request, "result.html", {'result': res})
    
    except:
        return HttpResponse("Please give your input")

    
    
