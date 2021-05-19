from leads.views import AssignAgentPage, CategoryListPage, LeadCreatePage, LeadDeletePage, LeadDetailPage, LeadListPage, LeadUpdateView
from django.urls.conf import include, path

app_name = "leads"

urlpatterns = [
    path('', LeadListPage.as_view(), name='lead_list' ),
    path("<int:pk>/", LeadDetailPage.as_view(), name='lead_detail'),
    path("<int:pk>/update", LeadUpdateView.as_view(), name='lead_update'),
    path("<int:pk>/delete", LeadDeletePage.as_view(),name='lead_delete' ),
    path("<int:pk>/assign-agent", AssignAgentPage.as_view(),name='assign_agent' ),
    path("create/", LeadCreatePage.as_view(),name='lead_create'),
    path("categories/", CategoryListPage.as_view(), name='category_list'),
]
