from django.shortcuts import render
from django.http import HttpResponse
import re

# Create your views here.

def string_times_view(request, string, n):
    if n >= 0:
        return HttpResponse(string * n)
    else:
        return HttpResponse("n must be positive")
    
def count_hi_view(request, string):
    return HttpResponse(string.count("hi"))

def count_code_view(request, string):
    return HttpResponse(len(re.findall("co.e", string, re.IGNORECASE)))