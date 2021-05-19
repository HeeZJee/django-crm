from agents.mixins import OraganisorLoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.forms import  AssignAgentForm, LeadModelForm, CustomUserCreationForm
from django.core.mail import send_mail
from django.shortcuts import  reverse
from leads.models import  Agent, Category, Lead
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
    context_object_name = "leads"

    def get_queryset(self):
        user = self.request.user
    
        if user.is_organisor:
            queryset = Lead.objects.filter(
                organisation= user.userprofile,
                agent__isnull = False,
                )
        else:
            queryset = Lead.objects.filter(
                organisation= user.agent.organisation,
                agent__isnull = False
                )
        
        queryset = queryset.filter(agent__user= user)
        return queryset
    
    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super(LeadListPage, self).get_context_data(**kwargs)      
          
        if user.is_organisor:
            
            queryset = Lead.objects.filter(
                organisation= user.userprofile,
                agent__isnull = True,
                )
            context.update({
                "unassigned_leads": queryset
            })
        return context
     
class LeadDetailPage(LoginRequiredMixin,generic.DetailView):
    template_name = 'leads/lead_detail.html'    
    context_object_name = "lead"

    def get_queryset(self):
        user = self.request.user
    
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation= user.userprofile )
        else:
            queryset = Lead.objects.filter(organisation= user.agent.organisation)
        
        queryset = queryset.filter(agent__user= user)
        return queryset


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
        return super(LeadCreatePage, self).form_valid(form)

class LeadUpdateView(OraganisorLoginRequiredMixin,generic.UpdateView):
    template_name = "leads/lead_update.html"            
    form_class = LeadModelForm


    def get_success_url(self): 
        return reverse('leads:lead_list')
    
    def get_queryset(self):
        user = self.request.user
    
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation= user.userprofile )
        else:
            queryset = Lead.objects.filter(organisation= user.agent.organisation)
        
        queryset = queryset.filter(agent__user= user)
        return queryset

class LeadDeletePage(OraganisorLoginRequiredMixin,generic.DeleteView):
    template_name = "leads/lead_delete.html"   
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead_list')
    
    def get_queryset(self):
        user = self.request.user    
        queryset = Lead.objects.filter(organisation= user.userprofile )        
        return queryset
    
class AssignAgentPage(OraganisorLoginRequiredMixin, generic.FormView):
    template_name = 'leads/assign_agent.html'
    form_class = AssignAgentForm
    
    def get_form_kwargs(self, **kwargs):
        kwargs = super(AssignAgentPage, self).get_form_kwargs(**kwargs)
        kwargs.update({ "request": self.request })
        return kwargs
    
    def get_success_url(self):
        return reverse('leads:lead_list')

    def form_valid(self, form):
        ## grap the agent from form
        ## grap the lead by "id from self kwargs" from model
        ## assign agent to lead
        agent = form.cleaned_data["agent"]
        lead = Lead.objects.get(id=self.kwargs['pk'])
        lead.agent = agent
        lead.save()
        return super(AssignAgentPage, self).form_valid(form)
    
class CategoryListPage(LoginRequiredMixin, generic.ListView):
    template_name = "leads/category_list.html"
    context_object_name = "category_list"

    def get_context_data(self,**kwargs):
        context = super(CategoryListPage, self).get_context_data(**kwargs)
        user = self.request.user

        if user.is_organisor:
            queryset = Lead.objects.filter(
                organisation=user.userprofile,
            )
        else:
            queryset = Lead.objects.filter(
                organisation=user.agent.organisation,
            )
        
        unassigned_lead_count = queryset.filter(category__isnull=True).count()
        context.update({
            "unassigned_lead_count": unassigned_lead_count
        })
        
        return context
    
    
    def get_queryset(self):
        user = self.request.user

        if user.is_organisor:
            queryset = Category.objects.filter(
                organisation= user.userprofile,
                )
        else:
            queryset = Category.objects.filter(
                organisation= user.agent.organisation,
                )        
        return queryset
