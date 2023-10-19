"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from rest_framework.routers import DefaultRouter

from .views import api, jwt, user


router = DefaultRouter()

router.register(r'users', user.UserViewSet)

urlpatterns = (
    [
        path('admin/', admin.site.urls),
        re_path('^ping/', api.ping),
        re_path(
            '^auth/login/', jwt.JWTObtainPairView.as_view(), name="token_obtain_pair"
        ),
        re_path(
            '^auth/token/refresh/',
            jwt.JWTRefreshView.as_view(),
            name="token_refresh",
        ),
        re_path('^', include(router.urls)),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)


if settings.APP_ENV == 'local' and not settings.DEBUG:
    urlpatterns.append(
        re_path(
            r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}
        )
    )
