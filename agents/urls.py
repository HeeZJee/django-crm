from agents.views import AgentCreateView, AgentDetailView, AgentListView
from django.urls import path
app_name = "agents"
urlpatterns = [
path("", AgentListView.as_view(), name="agent_list"),
path("create/", AgentCreateView.as_view(), name="agent_create"),
path("<int:pk>", AgentDetailView.as_view(), name="agent_detail"),
]