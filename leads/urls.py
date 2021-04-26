









from leads.views import lead_detail, lead_list
from django.urls.conf import include, path

app_name = "leads"

urlpatterns = [
    path('', lead_list ),
    path("<pk>/", lead_detail)
]
