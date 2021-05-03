from leads.views import LandingPageView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin 
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", LandingPageView.as_view(), name='landing_page'), 
    path('leads/', include("leads.urls",namespace="leads") ),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_ROOT, document_root=settings.STATIC_ROOT)
    
    