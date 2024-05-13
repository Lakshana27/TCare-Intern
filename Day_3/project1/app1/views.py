from django.shortcuts import render
from django.http import HttpResponse

def Hello(request): 
    my_message = '<h1> Welcome Everyone </h1>\
                  <p> Lets Make Fun Guys'
    return HttpResponse(my_message)