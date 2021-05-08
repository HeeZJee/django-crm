from agents.mixins import OraganisorLoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.forms import  LeadModelForm, CustomUserCreationForm
from django.core.mail import send_mail
from django.shortcuts import  reverse
from leads.models import  Lead
from django.views import  generic


class SignupView(LoginRequiredMixin,generic.CreateView):
    template_name = "registration/signup.html"            
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('login')

class LandingPageView(generic.TemplateView):
    template_name = "landing.html"

class LeadListPage(LoginRequiredMixin,generic.ListView):
    template_name = 'leads/lead_list.html'
    queryset = Lead.objects.all()
    context_object_name = "leads"


class LeadDetailPage(LoginRequiredMixin,generic.DetailView):
    template_name = 'leads/lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = "lead"



class LeadCreatePage(OraganisorLoginRequiredMixin,generic.CreateView):
    template_name = "leads/lead_create.html"            
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead_list')
    
    def form_valid(self, form):
        send_mail(
            subject="Lead Created",
            message="The lead has been created on your CRM. Please! visit to check your lead.",
            from_email="hafeezghanchi927@gmail.com",
            recipient_list=['hafeezghanchi927@gmail.com']   
            )
        return super(LeadCreatePage,self).form_valid(form)

class LeadUpdateView(OraganisorLoginRequiredMixin,generic.UpdateView):
    template_name = "leads/lead_update.html"            
    queryset = Lead.objects.all()
    form_class = LeadModelForm


    def get_success_url(self): 
        return reverse('leads:lead_list')

class LeadDeletePage(OraganisorLoginRequiredMixin,generic.DeleteView):
    template_name = "leads/lead_delete.html"   
    queryset = Lead.objects.all()         
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead_list')