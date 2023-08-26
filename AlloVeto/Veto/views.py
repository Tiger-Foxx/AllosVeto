from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from Veto.forms import *
from Veto.models import *
# Create your views here.

def index(request):
    info=informations.objects.all()
    if request.method == 'POST':
        form = RendezVousForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'veto/contact_succes.html',context= {'form': form,"infos":info})
        else :
            return render(request, 'veto/contact_fail.html',context= {'form': form,"infos":info})
    else:
        form = RendezVousForm()
    post=Post.objects.all()
    faq=FAQ.objects.all()
    partner=Partner.objects.all()
    team=Team.objects.all()
    whagroup=WhaGroup.objects.all()
    temoignage=Temoignage.objects.all()
    service=Service.objects.all()
    return render(request,'veto/index.html',context={"infos":info,"services":service,"temoignages":temoignage,"whagroups":whagroup,"posts":post,"FAQs":faq,"teams":team,"form":form,"partners":partner})

def consultation(request):
    info=informations.objects.all()
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'veto/contact_succes.html',context= {'form': form,"infos":info})
        else :
            return render(request, 'veto/contact_fail.html',context= {'form': form,"infos":info})
    else:
        form = ConsultationForm()
    return render(request, 'veto/diagnostique.html',context= {'form': form,"infos":info})
