from django.http import HttpResponse
from django.shortcuts import render
from leads.models import Lead

# Create your views here.
def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads/index.html", context)


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, "leads/leads_detail.html", context)

