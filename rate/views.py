# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from rate.models import prof
from django.shortcuts import render_to_response
from django import forms


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

def department(request, department):
    list_of_profs = prof.objects.filter(department=department.upper())
    return render_to_response('rate/index.html',
                              {'list_of_profs': list_of_profs})

# def prof_id(request, id):
#     list_of_profs = prof.objects.filter(id=id)
#     return render_to_response('rate/prof.html',
#                               {'list_of_profs': list_of_profs})





class ContactForm(forms.Form):
    coolness = forms.IntegerField()
    knowledge = forms.IntegerField()
    looks = forms.IntegerField()

def prof_id(request, id):
    p = prof.objects.filter(id=id)[0]
    pr = val = None
    if p.coolness and p.knowledge and p.looks:
        val = p
    else:
        pr = p

    if request.method == 'GET':
        form = ContactForm(request.GET)
        submit(p, form)
    else:
        form = ContactForm()

    return render_to_response('rate/prof.html', {'prof': pr, 'form': form, 'val': val})


def submit(prof, form):
    if form.is_valid():
        prof.coolness = form.cleaned_data['coolness']
        prof.knowledge = form.cleaned_data['knowledge']
        prof.looks = form.cleaned_data['looks']
        prof.save()

        return HttpResponseRedirect('/rate/'+str(prof.id)+'/')
