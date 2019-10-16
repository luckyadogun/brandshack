from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('how-it-works/', views.how_it_works, name='how-it-works'),
    path('samples/', views.samples, name='samples'),
    path('pricing/', views.pricing, name='pricing'),
]

urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)