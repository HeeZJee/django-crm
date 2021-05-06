from agents.views import AgentCreateView, AgentListView
from django.urls import path
app_name = "agents"
urlpatterns = [
path("", AgentListView.as_view(), name="agent_list"),
path("create/", AgentCreateView.as_view(), name="agent_create"),
]