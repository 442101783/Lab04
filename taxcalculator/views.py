from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def default_view(request):
    return render(request,'default.html')

def any_number_view(request, number):
    total_with_tax = number * 1.15
    result = {'total_with_tax': total_with_tax}
    return render(request, 'any_number.html',result)

def tax_rate_view(request):
    tax_rate = 15 
    result = {'tax_rate': tax_rate}
    return render(request,'tax_rate.html',result)
