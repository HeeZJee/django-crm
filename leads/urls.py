









from leads.views import lead_create, lead_delete, lead_detail, lead_list, lead_update
from django.urls.conf import include, path

app_name = "leads"

urlpatterns = [
    path('', lead_list, name='lead_list' ),
    path("<int:pk>/", lead_detail, name='lead_detail'),
    path("create", lead_create,name='lead_create'),
    path("<int:pk>/update", lead_update, name='lead_update'),
    path("<int:pk>/delete", lead_delete,name='lead_delete' ),
]
