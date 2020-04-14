"""middleware URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework import routers
from api import views
from rest_framework_extensions.routers import NestedRouterMixin
from . import settings

class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    pass

v1_router = NestedDefaultRouter()
v1_router.register(r'profile', views.ProfileViewSet)
questions = v1_router.register(r'trivia', views.TriviaViewSet)
questions.register(
    r'questions',
    views.QuestionViewSet,
    basename="questions",
    parents_query_lookups=['category', 'type']
)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('docs/', TemplateView.as_view(template_name="index.html")),
    path('inside/', admin.site.urls),
    path('api/v1/', include(v1_router.urls)),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken'))
    ] +  static(settings.STATIC_URL)
