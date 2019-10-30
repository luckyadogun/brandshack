from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('how-it-works/', views.how_it_works, name='how-it-works'),
    path('samples/', views.samples, name='samples'),
    path('pricing/', views.pricing, name='pricing'),
    path('team/', views.team, name='team'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('successful/', views.successful_trans, name='success-transaction'),
    path('failed/', views.failed_trans, name='failed-transaction'),
    path('activate-account/', views.activate_account, name='activate-account'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
]

urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)