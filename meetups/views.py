# views.py for index.html
# -------------------------------------
from django.shortcuts import render
#from django.http import HttpResponse


def index(request):
    meetups = [     #define a variable for exporting
        { 
            'title': 'A Ftrst Meetup', 
            'location': 'New York', 
            'slug': 'a-first-meetup' 
        },
        { 
            'title': 'A Second Meetup', 
            'location': 'Paris', 
            'slug': 'a-second-meetup' 
        }
    ]
    #return HttpResponse('Hello world')
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups  #var defined earlier as diconary
    })
    
def meetup_details(request, meetup_slug):
    selected_meetup = {
            'title': 'A First Meetup', 
            'description': 'This is the first meetup!'
            }
    return render(request, 'meetups/meetup-details.html', {
        'meetup_title': selected_meetup['title'],
        'meetup_description': selected_meetup['description']    
    })