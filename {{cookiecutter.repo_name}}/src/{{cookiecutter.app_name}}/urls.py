from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static

urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name="index.html"), name="home"),
    url(r'^admin/', include(admin.site.urls)),
]
