from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from penai import views

urlpatterns = [
    path('', views.name_gen, name='name-gen'),
]

urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)