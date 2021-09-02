# views.py for index_part_01.html
# -------------------------------------
from django.shortcuts import render
#from django.http import HttpResponse


def index(request):
    meetups = [     #define a variable for exporting
        { 'title': 'A Ftrst Meetup'},
        { 'title': 'A Second Meetup'}
    ]
    #return HttpResponse('Hello world')
    return render(request, 'meetups/index_part_01.html', {
        'show_meetups': True,
        'meetups': meetups  #var defined earlier as diconary
    })
    