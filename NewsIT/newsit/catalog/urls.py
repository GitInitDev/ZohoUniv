# Use include() to add paths from the catalog application
from django.urls import include
from django.urls import path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns += [
    path('catalog/', include('catalog.urls')),
]
# Add URL maps to redirect the base URL to our application
urlpatterns += [
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
]
# Use static() to add url mapping to serve static files during development (only)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url='catalog/')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = [

]