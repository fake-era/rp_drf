from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from config.settings.components.common import DEBUG  # , MEDIA_ROOT, MEDIA_URL

api_urlpatterns = [
    path('pizza/', include('apps.pizza.api.urls')),
    path('restaurant/', include('apps.restaurant.api.urls')),
    path('order/', include('apps.order.api.urls'))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(
        (api_urlpatterns, 'admin_api_urlpatterns'),
        namespace='admin_api_urlpatterns'))
]


if DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
