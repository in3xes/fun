# Create your views here.

from django.http import HttpResponse
from rate.models import prof
from django.shortcuts import render_to_response

def index(request):
    list_of_profs = prof.objects.all()
    return render_to_response('rate/index.html',
                              {'list_of_profs': list_of_profs})

def institute(request, institute):
    list_of_profs = prof.objects.filter(institute=institute.upper())
    return render_to_response('rate/index.html',
                              {'list_of_profs': list_of_profs})

def inst_dept(request, institute, department):
    list_of_profs = prof.objects.filter(institute=institute.upper(),
                                        department=department.upper())
    return render_to_response('rate/index.html',
                              {'list_of_profs': list_of_profs})
