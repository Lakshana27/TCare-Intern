from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def party_time(request):
    start_time = datetime.now()
    return HttpResponse('<h1> Party Time : </h1>' + str(start_time))
