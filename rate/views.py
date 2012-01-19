# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
from rate.models import prof
from django.shortcuts import render_to_response
from django import forms


def index(request):
    list_of_profs = prof.objects.all()
    return render_to_response('rate/index.html',
                              {'list_of_profs': list_of_profs})

def institute(request, institute):
    list_of_profs = prof.objects.filter(institute=institute.upper())
    if len(list_of_profs) == 0:
        raise Http404
    return render_to_response('rate/index.html',
                              {'list_of_profs': list_of_profs})

def inst_dept(request, institute, department):
    list_of_profs = prof.objects.filter(institute=institute.upper(),
                                        department=department.upper())
    if len(list_of_profs) == 0:
        raise Http404
    return render_to_response('rate/index.html',
                              {'list_of_profs': list_of_profs})

def department(request, department):
    if len(list_of_profs) == 0:
        raise Http404
    list_of_profs = prof.objects.filter(department=department.upper())
    return render_to_response('rate/index.html',
                              {'list_of_profs': list_of_profs})


class RatingForm(forms.Form):
    coolness = forms.IntegerField()
    knowledge = forms.IntegerField()
    looks = forms.IntegerField()

def prof_display(request, id):
    try:
        p = prof.objects.filter(id=id)[0]
    except:
        raise Http404
        # return HttpResponseNotFound('<h1>Page not found</h1>')

    form = RatingForm
    if p.coolness and p.knowledge and p.looks:
        return render_to_response('rate/prof.html', {'prof': p})
    else:
        return render_to_response('rate/prof_rate.html', {'prof': p,
                                                 'form': form})
                                                 

def submit(request, id):
    
    if request.method == 'GET':
        p = prof.objects.filter(id=id)[0]
        form = RatingForm(request.GET)
        if form.is_valid():
            p.coolness = form.cleaned_data['coolness']
            p.knowledge = form.cleaned_data['knowledge']
            p.looks = form.cleaned_data['looks']
            p.save()
        return HttpResponseRedirect('/rate/'+str(id)+'/')
    else:
        return HttpResponseRedirect('/rate/'+str(id)+'/')
