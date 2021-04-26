









from leads.views import lead_create, lead_detail, lead_list
from django.urls.conf import include, path

app_name = "leads"

urlpatterns = [
    path('', lead_list ),
    path("<int:pk>/", lead_detail),
    path("create", lead_create),
]
