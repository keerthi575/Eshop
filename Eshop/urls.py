from django.contrib import admin
from django.urls import path  , include
from django.conf.urls.static import static
from . import settings
# dj_razorpay/urls.py
from payment import views

urlpatterns = [
	path('', views.homepage, name='index'),
	path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
	path('admin/', admin.site.urls),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('store.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
