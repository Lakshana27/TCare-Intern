from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, time

def welcome(request):
    current_time = datetime.now().time()
    if time(6,0,0) <= current_time < time(12,0,0):
        message = "<h1>Good morning, dear. Have a great day!<h1>"
    elif time(12,0,0) <= current_time < time(17,0,0):
        message = "Good Afternoon, dear. Had Lunch?"
    elif time(17,0,0) <= current_time < time(19,0,0):
        message = "Good Evening, dear. Dont Waste your time"
    elif time(19,0,0) <= current_time < time(24,0,0):
        message = "Good Night, dear. Have a tight sleep"
    
    result = message + f"<h2>{current_time.strftime('%I:%M:%p')}</h2>"
    return HttpResponse(result)
    


    






# def welcome(request):
#     current_time = datetime.now().time()
#     if current_time >= datetime.strptime('05:00:00', '%H:%M:%S').time() and current_time < datetime.strptime('12:00:00', '%H:%M:%S').time():
#         return HttpResponse('<h1>Good morning!</h1>')
#     elif current_time >= datetime.strptime('12:00:00', '%H:%M:%S').time() and current_time < datetime.strptime('16:00:00', '%H:%M:%S').time():
#         return HttpResponse('<h1>Good Afternoon!</h1>')
#     elif current_time >= datetime.strptime('16:00:00', '%H:%M:%S').time() and current_time < datetime.strptime('19:00:00', '%H:%M:%S').time():
#         return HttpResponse('<h1>Good Evening!</h1>')
#     elif current_time >= datetime.strptime('19:00:00', '%H:%M:%S').time() and current_time < datetime.strptime('24:00:00', '%H:%M:%S').time():
#         return HttpResponse('<h1>Good Evening!</h1>')