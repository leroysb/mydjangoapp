from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('django.contrib.auth.urls')),
    path('account/',include('account.urls')),
    path('', include('core.urls')),
]

if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'core.errorviews.page404'
handler500 = 'core.errorviews.page500'
# handler403 = 'mysite.views.my_custom_permission_denied_view' # Permission denied
# handler400 = 'mysite.views.my_custom_bad_request_view' # Bad request