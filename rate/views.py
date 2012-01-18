# Create your views here.

from django.http import HttpResponse
from rate.models import prof
from django.shortcuts import render_to_response

def index(request):
    list_of_profs = prof.objects.all()
    # matrix = [[p.name, p.institute, p.department, p.website, p.email, str(p.coolness)] for p in list_of_profs]
    # output = [', '.join(p) for p in matrix]
    # return HttpResponse(output)
    return render_to_response('rate/index.html', {'list_of_profs': list_of_profs})
