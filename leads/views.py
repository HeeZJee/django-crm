from django.forms.forms import Form
from leads.forms import LeadForm, LeadModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from leads.models import Agent, Lead

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
    return render(request, "leads/lead_detail.html", context)

    

def lead_create(request):
    form = LeadModelForm()

    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")

    context = {
        "form": form
    }

    return render(request, "leads/lead_create.html", context)


def lead_update(request,pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)

    if request.method == "POST":
        form = LeadModelForm(request.POST,instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context ={
        "lead": lead,
        "form" : form
    }
    return render(request,"leads/lead_update.html",context)

# def lead_create(request):
#     form = LeadForm()

#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data["last_name"]
#             age = form.cleaned_data["age"]
#             agent = form.cleaned_data["agent"]

#             Lead.objects.create(
#                 first_name=first_name,
#                 last_name=last_name,
#                 age= age,
#                 agent= agent
#                  )
#             print(f"Lead {first_name} {last_name} added to db.")
#             return redirect("/leads")

#     context = {
#         "form": form
#     }

#     return render(request, "leads/lead_create.html", context)
