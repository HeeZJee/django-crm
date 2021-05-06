from agents.views import AgentListView
from django.urls import path
app_name = "agents"
urlpatterns = [
path("", AgentListView.as_view(), name="agent_list")
]