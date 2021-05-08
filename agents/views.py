from agents.forms import  AgentModelForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from django.urls import reverse
# Create your views here.
class AgentListView(LoginRequiredMixin, generic.ListView):
    template_name = "agents/agent_list.html"
    context_object_name = 'agents'
    
    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)
    
class AgentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm
    
    def get_success_url(self):  
        return reverse("agents:agent_list")
    
    def form_valid(self,form):
        agent = form.save(commit = False)
        agent.organisation = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView,self).form_valid(form)
    
    
class AgentDetailView(LoginRequiredMixin,generic.DetailView):
    template_name = 'agents/agent_detail.html'
    context_object_name = 'agent'
    
    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)

class AgentUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'agents/agent_update.html'
    context_object_name = 'agent'
    form_class = AgentModelForm

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)
    
    def get_success_url(self):   
        return reverse("agents:agent_list")
    
class AgentDetailView(LoginRequiredMixin,generic.DetailView):
    template_name = 'agents/agent_detail.html'
    context_object_name = 'agent'
    
    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)
    
class AgentDeleteView(LoginRequiredMixin,generic.DeleteView):
    template_name = "agents/agent_delete.html"   
    context_object_name = 'agent'

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)
    
    def get_success_url(self):   
        return reverse("agents:agent_list")